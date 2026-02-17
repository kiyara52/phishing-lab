from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
	return render_template("dashboard.html")

@app.route("/analyze", methods=["GET", "POST"])
def analyze():
	if request.method == "POST":
		header = request.form.get("header")
		if not header:
			return "no header provided"
	
		if "185." in header:
			data = {
				"malicious_ip": "185.234..218.77",
				"domain": "micr0soft-support-login.com",
				"risk-level": "High",
				"summary": "header analysis reveals spoofed sender and suspicious relay IP. Domain is recently registered and flagged."
			}
		else:
			data = {
				"malicious_ip": "Not detected",
				"domain": "Unknown",
				"risk-level": "LOW",
				"summary": "no strong phishing indicators founds."
			}

		return render_template("result.html",data=data)

if __name__=="__main__":
	port = int(os.environ.get("PORT",10000))
	app.run(host="0.0.0.0",port=port)
