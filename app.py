from flask import Flask, render_template, request, jsonify

# Flask app setup
app = Flask(__name__)

@app.route("/")
def index():
    """Serve the calculator homepage."""
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    """
    Receives a math expression from the frontend (via AJAX/fetch),
    evaluates it safely, and returns the result as JSON.
    """
    data = request.get_json()          # parse JSON body from frontend
    expression = data.get("expression", "")

    try:
        # eval() runs the math expression string as Python code
        # We restrict the allowed names for safety (no imports, no builtins abuse)
        allowed_names = {"__builtins__": {}}
        result = eval(expression, allowed_names)
        return jsonify({"result": str(result), "error": None})
    except ZeroDivisionError:
        return jsonify({"result": None, "error": "Cannot divide by zero"})
    except Exception as e:
        return jsonify({"result": None, "error": "Invalid expression"})

if __name__ == "__main__":
    # debug=True means Flask auto-reloads when you save changes
    app.run(debug=True)
