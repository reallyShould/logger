import logging
from logging.handlers import DatagramHandler
from flask import Flask

app = Flask(__name__)

class UDPSocketHandler(DatagramHandler):
    def makePickle(self, record):
        return self.format(record).encode('utf-8')

UDP_IP = "127.0.0.1"
UDP_PORT = 5140

logger = logging.getLogger("udp_logger")
logger.setLevel(logging.DEBUG)

udp_handler = UDPSocketHandler(UDP_IP, UDP_PORT)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
udp_handler.setFormatter(formatter)

logger.addHandler(udp_handler)

@app.route("/")
def home():
    logger.debug("Debug message: Home route accessed")
    logger.info("Info message: Home route accessed")
    logger.warning("Warning message: Home route accessed")
    logger.error("Error message: Home route accessed")
    logger.critical("Critical message: Home route accessed")
    return "Flask with logging!"

@app.route("/test")
def test():
    logger.debug("Debug message: Test route accessed")
    logger.info("Info message: Test route accessed")
    logger.warning("Warning message: Test route accessed")
    logger.error("Error message: Test route accessed")
    logger.critical("Critical message: Test route accessed")
    return "Test page"

if __name__ == "__main__":    
    app.run(debug=True)
