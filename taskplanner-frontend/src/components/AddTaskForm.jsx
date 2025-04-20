import { useState, useEffect } from 'react';

const AddTaskForm = ({ onTaskAdded, token }) => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [taskClass, setTaskClass] = useState('1');
    const [priority, setPriority] = useState('medium');
    const [completed, setCompleted] = useState(false);
    const [error, setError] = useState(null);
    const [taskClasses, setTaskClasses] = useState({});

    useEffect(() => {
        // Fetch task classes when component mounts
        const fetchTaskClasses = async () => {
            try {
                const response = await fetch("http://localhost:8000/api/task-classes/", {
                    headers: {
                        "Authorization": `Token ${token}`,
                    },
                });
                if (!response.ok) {
                    throw new Error("Failed to fetch task classes");
                }
                const data = await response.json();
                setTaskClasses(data);
            } catch (error) {
                console.error("Error fetching task classes:", error);
            }
        };

        fetchTaskClasses();
    }, [token]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);

        if (!title.trim()) {
            setError("Tehtävän nimi ei voi olla tyhjä.");
            return;
        }

        const newTask = {
            title,
            description,
            task_class: taskClass,
            priority,
            completed,
        };

        try {
            const response = await fetch("http://localhost:8000/api/tasks/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Token ${token}`,
                },
                body: JSON.stringify(newTask),
            });

            if (!response.ok) {
                throw new Error("Tehtävän lisääminen epäonnistui.");
            }

            const createdTask = await response.json();
            onTaskAdded(createdTask);
            // Reset form
            setTitle('');
            setDescription('');
            setTaskClass('1');
            setPriority('medium');
            setCompleted(false);
        } catch (error) {
            setError(error.message);
        }
    };

    return (
        <div className="add-task-form">
            <h2>Lisää uusi tehtävä</h2>
            {error && <p style={{color: "red"}}>{error}</p>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Tehtävän nimi:</label>
                    <input
                        type="text"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                    />
                </div>
                <div>
                    <label>Kuvaus:</label>
                    <textarea
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                    />
                </div>
                <div>
                    <label>Tehtäväluokka:</label>
                    <select
                        value={taskClass}
                        onChange={(e) => setTaskClass(e.target.value)}
                    >
                        {Object.entries(taskClasses).map(([value, label]) => (
                            <option key={value} value={value}>
                                {label}
                            </option>
                        ))}
                    </select>
                </div>
                <div>
                    <label>Prioriteetti:</label>
                    <select
                        value={priority}
                        onChange={(e) => setPriority(e.target.value)}
                    >
                        <option value="low">Matala</option>
                        <option value="medium">Keskitaso</option>
                        <option value="high">Korkea</option>
                    </select>
                </div>
                <div className="checkbox-group">
                    <label>
                        <input
                            type="checkbox"
                            checked={completed}
                            onChange={(e) => setCompleted(e.target.checked)}
                        />
                        Valmis
                    </label>
                </div>
                <button type="submit">Lisää tehtävä</button>
            </form>
        </div>
    );
};

export default AddTaskForm; 