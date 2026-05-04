@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Dummy credentials (for testing)
        if username == "admin" and password == "admin":
            app.logger.info("User logged in successfully")
            return "✅ Login Successful"
        else:
            app.logger.warning("Invalid login attempt")
            return "❌ Invalid Credentials"

    return '''
        <h2>Login Page</h2>
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''
