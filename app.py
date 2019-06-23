from url_shortener import create_application

if __name__ == "__main__":
    app = create_application()
    for handler, (rule, router) in app.router.routes_names.items():
        print('URL: ', rule)
    print()
    app.run(host="0.0.0.0", port=8000, debug=True)
