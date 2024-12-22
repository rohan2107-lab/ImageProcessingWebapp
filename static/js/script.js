// Add live file upload feedback
document.querySelector('input[type="file"]').addEventListener('change', function () {
    const fileName = this.files[0]?.name || "No file selected";
    alert(`Selected file: ${fileName}`);
});

// Ensure width and height values are positive
document.querySelector('form[action="/resize"]').addEventListener('submit', function (e) {
    const width = parseInt(this.querySelector('input[name="width"]').value, 10);
    const height = parseInt(this.querySelector('input[name="height"]').value, 10);
    if (width <= 0 || height <= 0) {
        alert("Width and Height must be positive values.");
        e.preventDefault();
    }
});
// Theme Toggle
const themeToggle = document.getElementById('theme-toggle');
themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark');
});

// Clear Forms
document.getElementById('clear-upload').addEventListener('click', () => {
    document.getElementById('upload-form').reset();
    imagePreview.innerHTML = '';
});

document.getElementById('clear-resize').addEventListener('click', () => {
    document.getElementById('resize-form').reset();
});

