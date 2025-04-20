import React, { useEffect, useState } from "react";
import { getTasks, updateTask } from "./api/taskApi";
import AddTaskForm from "./components/AddTaskForm";
import './App.css';

function App() {
    const [tasks, setTasks] = useState([]);
    const [editingTask, setEditingTask] = useState(null);
    const [showForm, setShowForm] = useState(false);
    const token = "c299d6e148827f85fffef091d89e2a9f70153994";

    useEffect(() => {
        fetchTasks();
    }, []);

    const fetchTasks = async () => {
        const data = await getTasks(token);
        setTasks(data);
    };

    const handleTaskAdded = (newTask) => {
        setTasks([...tasks, newTask]);
        setShowForm(false);
    };

    const handleStatusClick = async (task, e) => {
        e.stopPropagation();
        try {
            const updatedTask = {
                ...task,
                completed: !task.completed
            };
            await updateTask(token, task.id, updatedTask);
            fetchTasks();
        } catch (error) {
            console.error('Error updating task:', error);
        }
    };

    const getTasksByStatus = (status) => {
        return tasks.filter(task => {
            switch(status) {
                case 'Todo':
                    return !task.completed && task.task_class === '1';
                case 'In Progress':
                    return !task.completed && task.task_class === '2';
                case 'Done':
                    return task.completed;
                case 'Backlog':
                    return !task.completed && task.task_class === '4';
                default:
                    return false;
            }
        });
    };

    return (
        <div className="container">
            <h1 className="title">Task Planner</h1>
            <button className="add-task-button" onClick={() => setShowForm(!showForm)}>
                {showForm ? 'Sulje lomake' : '+ Uusi tehtävä'}
            </button>
            
            {showForm && (
                <AddTaskForm onTaskAdded={handleTaskAdded} token={token} />
            )}

            <div className="kanban-board">
                {['Todo', 'In Progress', 'Done', 'Backlog'].map(status => (
                    <div key={status} className="kanban-column">
                        <h2 className="column-title">{status}</h2>
                        <div className="task-list">
                            {getTasksByStatus(status).map(task => (
                                <div key={task.id} className="task-card">
                                    <h3>{task.title}</h3>
                                    <p>{task.description}</p>
                                    <div className="task-meta">
                                        <span className={`priority-tag ${task.priority}`}>
                                            {task.priority}
                                        </span>
                                        <span 
                                            className={`status-tag ${task.completed ? 'completed' : 'in-progress'}`}
                                            onClick={(e) => handleStatusClick(task, e)}
                                        >
                                            {task.completed ? 'Valmis' : 'Kesken'}
                                        </span>
                                    </div>
                                </div>
                            ))}
                            {getTasksByStatus(status).length === 0 && (
                                <p className="no-tasks">Ei tehtäviä</p>
                            )}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default App;
