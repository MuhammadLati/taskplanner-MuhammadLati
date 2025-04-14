import React, { useEffect, useState } from "react";
import { getTasks, updateTask } from "./api/taskApi";
import './App.css';

function App() {
    const [tasks, setTasks] = useState([]);
    const [editingTask, setEditingTask] = useState(null);
    const token = "c299d6e148827f85fffef091d89e2a9f70153994";

    useEffect(() => {
        fetchTasks();
    }, []);

    const fetchTasks = async () => {
        const data = await getTasks(token);
        setTasks(data);
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

    const handleEditClick = (task, e) => {
        e.stopPropagation();
        setEditingTask({ ...task });
    };

    const handleSaveEdit = async (e) => {
        e.preventDefault();
        try {
            await updateTask(token, editingTask.id, editingTask);
            setEditingTask(null);
            fetchTasks();
        } catch (error) {
            console.error('Error saving task:', error);
        }
    };

    return (
        <div className="container">
            <h1 className="title">Task Planner</h1>
            <div className="task-list">
                {tasks.map((task) => (
                    <div key={task.id} className="task-card">
                        {editingTask?.id === task.id ? (
                            <form onSubmit={handleSaveEdit} className="edit-form">
                                <input
                                    type="text"
                                    value={editingTask.title}
                                    onChange={(e) => setEditingTask({
                                        ...editingTask,
                                        title: e.target.value
                                    })}
                                    className="edit-input"
                                />
                                <textarea
                                    value={editingTask.description || ''}
                                    onChange={(e) => setEditingTask({
                                        ...editingTask,
                                        description: e.target.value
                                    })}
                                    className="edit-textarea"
                                />
                                <select
                                    value={editingTask.priority}
                                    onChange={(e) => setEditingTask({
                                        ...editingTask,
                                        priority: e.target.value
                                    })}
                                    className="edit-select"
                                >
                                    <option value="low">Low</option>
                                    <option value="medium">Medium</option>
                                    <option value="high">High</option>
                                </select>
                                <div className="edit-buttons">
                                    <button type="submit" className="save-button">Save</button>
                                    <button type="button" onClick={() => setEditingTask(null)} className="cancel-button">Cancel</button>
                                </div>
                            </form>
                        ) : (
                            <>
                                <h2 className="task-title">{task.title}</h2>
                                <p className="task-description">{task.description || ''}</p>
                                <div className="task-meta">
                                    <div className="priority-tag">
                                        Priority: {task.priority}
                                    </div>
                                    <div className="task-actions">
                                        <button 
                                            onClick={(e) => handleEditClick(task, e)}
                                            className="edit-button"
                                        >
                                            Edit
                                        </button>
                                        <div 
                                            className={`status-tag ${task.completed ? 'completed' : 'in-progress'}`}
                                            onClick={(e) => handleStatusClick(task, e)}
                                        >
                                            {task.completed ? 'Completed' : 'In Progress'}
                                        </div>
                                    </div>
                                </div>
                            </>
                        )}
                    </div>
                ))}
            </div>
        </div>
    );
}

export default App;
