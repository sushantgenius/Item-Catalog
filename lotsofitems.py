from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

#Created a database along with a alternative to update and items to the database

# Create database and create a shortcut for easier to update database
engine = create_engine('sqlite:///catalogs.db')
#Adding the engine into the metadata so the declarative can be esaily accessed
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
#DBSession() is the staging area to add all the objects inside the database

# A Trial User is created here
User1 = User(name="Divya Jha", email="tippydrip@gmail.com")
session.add(User1)
session.commit()

# Creating Item for Mobile Products
mobile = Categories(user_id=1, name="Mobile Devices")
session.add(mobile)
session.commit()


# Creating category for Notebook Products
notebook = Categories(user_id=1, name="Notebook")
session.add(notebook)
session.commit()

# Creating category for Tablet Products
tablet = Categories(user_id=1, name="Tablets")
session.add(tablet)
session.commit()

# Creating category for music player Products
musicplayer = Categories(user_id=1, name="Music Player")
session.add(musicplayer)
session.commit()

# Creating category for Desktop Products
desktop = Categories(user_id=1, name="Desktop")
session.add(desktop)
session.commit()

# Creating category for Storage Products
storage = Categories(user_id=1, name="Storage Devices")
session.add(storage)
session.commit()

# Creating category for DSLR Camera Products
dslr = Categories(user_id=1, name="DSLR Cameras")
session.add(dslr)
session.commit()


# Creating category for Mirrorless Camera Products
mirrorless = Categories(user_id=1, name="Mirrorless Cameras")
session.add(mirrorless)
session.commit()


# Creating category for Gaming Console Products
gaming = Categories(user_id=1, name="Gaming Console")
session.add(gaming)
session.commit()



# Now adding the items inside these categories to be stored
productItem1 = CategoryItem(user_id=1, name="Apple iPhone",
                             description="Apple is a status symbol for some\
                             it defines luxury to a whole new level\
                             it defines a character of class and perfection\
                             but this legacy is soon getting outcompeted by\
                             by Chinese manufacturers",
                             categories=mobile)
session.add(productItem1)
session.commit()

productItem1 = CategoryItem(user_id=1, name="Convertibles are new thing",
                             description="Samsung introduced the consumer\
                             electronics market with touchscreen laptop\
                             problem was it was not foldable so you cannot do much\
                             Now you can with HP convertible x 360 you can draw as well\
                             as type",
                             categories=notebook)
session.add(productItem1)
session.commit()

productItem1 = CategoryItem(user_id=1, name="Tablet transforming into PC",
                             description="With the introduction of Microsoft\
                             surface and tablet PC. The old school android tablet\
                             have seen their good days. People are demanding more\
                             from their devices and they want it more portable\
                             therefore in this narrative tablets are not fitting in.",
                             categories=tablet)
session.add(productItem1)
session.commit()

productItem1 = CategoryItem(user_id=1, name="Ipod is Dead",
                             description="Ipod a revolutanary product\
                             which changed the entire segment of listening\
                             devices finally sees its end in the near future\
                             with advanced phones and storage in them now it\
                             is not worthwhile to get one extra device for music",
                             categories=musicplayer)
session.add(productItem1)
session.commit()

productItem1 = CategoryItem(user_id=1, name="Trash-can Mac",
                             description="Apple is known to create\
                             beautiful products but this very time\
                             it lacked by producing over priced slow\
                             piece of trash which even a HP ministation\
                             can beat",
                             categories=desktop)
session.add(productItem1)
session.commit()

productItem1 = CategoryItem(user_id=1, name="SSD is Blazing Fast",
                             description="In the current world storage\
                             is everything from storing movies and files\
                             to storing your work software. SSD gives you\
                             the speed and reliability which we were looking\
                             for a very long time.",
                             categories=storage)
session.add(productItem1)
session.commit()

productItem1 = CategoryItem(user_id=1, name="DSLR Vs Mirrorless",
                             description="DSLR cameras have been around\
                             for a while the market leader canon introduced EOS\
                             series which is versatile and has so many lens choices.",
                             categories=dslr)
session.add(productItem1)
session.commit()

productItem1 = CategoryItem(user_id=1, name="Sony alpha series Cameras",
                             description="DSLR was ruling the picture world\
                             until the mirrorless technology popped in. Sony\
                             is the market leader in this segment which produces\
                             cameras which can even see in the low light.",
                             categories=mirrorless)
session.add(productItem1)
session.commit()

productItem1 = CategoryItem(user_id=1, name="PS-4",
                             description="PS-4 Developed by Sony has been around\
                             since 1990s. Started as wired not so popular console\
                             now it has taken over the world with thousands of games\
                             for the users to play and entertain",
                             categories=gaming)
session.add(productItem1)
session.commit()



print "Added category items!"
