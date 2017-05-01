from flask import Flask, render_template
app = Flask(__name__)

def read_temperature():
    f = open('/sys/bus/w1/devices/28-000003e0bf4a/w1_slave', 'r')
    lines = f.readlines()
    f.close()

    if len(lines) >= 2 and lines[0].strip()[-3:] == 'YES':
        temp_output = lines[1].find('t=')
        if temp_output != -1:
            temp_string = lines[1][temp_output+2:].strip()
            temp_c = float(temp_string) / 1000.0
            return temp_c
    return 'unknown'

@app.route("/")
def index():
    return render_template("index.html", temperature=read_temperature())

if __name__ == '__main__':
    app.run(port=8000)
