from webappflask import create_app

app = create_app()
# app.app_context().push()  # To push an application context


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
