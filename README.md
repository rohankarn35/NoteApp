# FastAPI Note Web App

![image](https://github.com/rohankarn35/NoteApp/assets/104725432/f2fe4468-a3ee-4822-8b9e-f587cd5a6570)


A simple note-taking web app built with FastAPI, MongoDB, Jinja, HTML, and Bootstrap. This app allows users to create, update, read, and delete notes.

## Features

- **Create Notes:** Easily add new notes with a title and description.
- **Update Notes:** Modify existing notes with an intuitive editing interface.
- **Read Notes:** View your notes with a clean and user-friendly interface.
- **Delete Notes:** Remove unwanted notes effortlessly.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- [MongoDB](https://www.mongodb.com/): A NoSQL database for storing and retrieving notes.
- [Jinja](https://jinja.palletsprojects.com/): A modern and designer-friendly templating engine for Python.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): The standard markup language for creating web pages.
- [Bootstrap](https://getbootstrap.com/): The world’s most popular front-end open-source toolkit.

## Getting Started

1. Clone the repository:

    ```bash
    git clone [https://github.com/rohankarn35/NoteApp.git
    cd NoteApp
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure MongoDB:

    Update the MongoDB connection string in `config/db.py`.

4. Run the FastAPI app:

    ```bash
    uvicorn index:app --reload
    ```

5. Open the app in your browser:

    Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.


## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
