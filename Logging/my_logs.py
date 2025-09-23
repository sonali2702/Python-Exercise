import logging

# Step 1: Configure logging once
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename='new_logs.logs'
)

logger = logging.getLogger(__name__)

# Step 2: Create a decorator
def logs(func):
    def wrapper():
        logger.info("Before the function runs")
        func()
        logger.info("After the function runs")
    return wrapper

