import restcontroller

# this is to support uWSGI/nginx/apache
app = restcontroller.fapp

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
