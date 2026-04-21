document.addEventListener('DOMContentLoaded', function() {
    const newTaskButton = document.getElementById('newTaskButton');
    const taskList = document.getElementById('task-list');

    // Fetch tasks from the backend
    fetch('/tasks')
        .then(response => response.json())
        .then(tasks => {
            taskList.innerHTML = ''; // Clear existing tasks
            tasks.forEach(task => {
                const taskElement = document.createElement('div');
                taskElement.textContent = `${task.title} - ${task.description}`;
                taskList.appendChild(taskElement);
            });
        })
        .catch(error => console.error('Error fetching tasks:', error));

    // Create new task
    newTaskButton.addEventListener('click', () => {
        const title = prompt("Enter task title:");
        const description = prompt("Enter task description:");
        if (title && description) {
            const newTask = { title: title, description: description };
            fetch('/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(newTask)
            })
            .then(response => response.json())
            .then(createdTask => {
                // Update the task list with the new task
                taskList.innerHTML = '';
                fetch('/tasks')
                    .then(response => response.json())
                    .then(tasks => {
                        tasks.forEach(task => {
                            const taskElement = document.createElement('div');
                            taskElement.textContent = `${task.title} - ${task.description}`;
                            taskList.appendChild(taskElement);
                        });
                    });
            })
            .catch(error => console.error('Error creating task:', error));
        }
    });
});