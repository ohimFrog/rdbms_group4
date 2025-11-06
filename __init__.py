# This file ensures the models are imported and registered with SQLAlchemy Base
from database import Base
import models

# Import all models to register them with Base
__all__ = ['Base', 'models']
