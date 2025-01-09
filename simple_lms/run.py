from app import create_app

# Create the Flask app instance using the factory function
app = create_app()

if __name__ == '__main__':
    # Run the app with debugging enabled
    app.run(debug=True, host='127.0.0.1', port=5000)
