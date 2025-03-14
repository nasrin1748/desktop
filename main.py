from flask import Flask, jsonify
from IPython.display import HTML, display
import threading
import socket
import webbrowser

# Create Flask app
app = Flask(__name__)


# Define routes
@app.route('/')
def home():
    return '''
    <h1>Development Server</h1>
    <p>Server is running successfully!</p>
    <ul>
        <li><a href="/api/test">Test API Endpoint</a></li>
        <li><a href="/health">Health Check</a></li>
    </ul>
    '''


@app.route('/api/test')
def test_api():
    return jsonify({
        "status": "success",
        "message": "API is working"
    })


@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "server": "running"
    })


# Function to get available port
def get_free_port():
    sock = socket.socket()
    sock.bind(('', 0))
    port = sock.getsockname()[1]
    sock.close()
    return port


# Start server function
def start_server(port):
    app.run(port=port, debug=True, use_reloader=False)


# Main execution
if __name__ == '__main__':
    # Get available port
    port = get_free_port()

    # Start server in a separate thread
    server_thread = threading.Thread(target=start_server, args=(port,))
    server_thread.daemon = True
    server_thread.start()

    # Display server information
    server_url = f"http://localhost:{port}"
    display(HTML(f"""
        <div style="padding: 20px; background-color: #f0f0f0; border-radius: 5px;">
            <h3>Development Server Started</h3>
            <p>Server URL: <a href="{server_url}" target="_blank">{server_url}</a></p>
            <p>Available endpoints:</p>
            <ul>
                <li>{server_url}/ (Home)</li>
                <li>{server_url}/api/test (Test API)</li>
                <li>{server_url}/health (Health Check)</li>
            </ul>
        </div>
    """))

    # Open browser automatically
    webbrowser.open(server_url)
