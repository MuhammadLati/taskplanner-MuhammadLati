import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/tasks/";

export const getTasks = async (token) => {
    try {
        const response = await axios.get(API_URL, {
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json',
            }
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching tasks:', error);
        throw error;
    }
};

export const updateTask = async (token, taskId, updatedData) => {
    const response = await axios.put(`${API_URL}${taskId}/`, updatedData, {
        headers: { 
            'Authorization': `Token ${token}`,
            'Content-Type': 'application/json',
        },
    });
    return response.data;
}; 