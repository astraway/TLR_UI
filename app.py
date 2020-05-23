from aquaui import app
import os

if __name__ == '__main__':
    #for deployment via docker to aws
    #app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

    #for running locally
    app.run(debug=True )

