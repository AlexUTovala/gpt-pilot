from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=8080) // INPUT_REQUIRED {Choose a different port if 5000 is in use}
