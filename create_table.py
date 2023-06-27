from sqlalchemy import create_engine, Column, Integer, String,DateTime, DECIMAL, Date

from sqlalchemy.orm import sessionmaker, declarative_base

# Define the model
Base = declarative_base()

# class merchant_info(Base):

#     __tablename__                              ="merchants"
#     id                                         = Column(Integer,autoincrement=True ,primary_key=True)
#     timestamp                                  = Column(DateTime, nullable=True)
#     no                                         =Column(Integer, primary_key=True)
#     bde_name                                    =Column(String(255),nullable = True)
#     business_structure	                        = Column(String(255),nullable = True)
#     shop_name	                                =Column(String(255),nullable = True)
#     percentage_of_commission_offered_to_xpayback=Column(DECIMAL, nullable = True)
#     business_address                            =Column(String(255), nullable=True)
#     owner_full_name                             =Column(String(50), nullable=True)
#     owner_contact_number                        =Column(String(20), nullable=True, unique=True)
#     shop_category                               = Column(String,nullable = True)
#     lead_stage	                                =Column(String(255),nullable = True)
#     corporate_or_registration_name              =Column(String(255),nullable = True)
#     pincode                                     =Column(String(255),nullable = True)
#     district                                    =Column(String(255),nullable = True)
#     state	                                    =Column(String(255),nullable = True)
#     pan_number                                  =Column(String(255),nullable = True)
#     gst_number                                  =Column(String(255),nullable = True)
#     merchant_upi_id                             =Column(String(255),nullable = True)
#     company_description	                        =Column(String(255),nullable = True)
#     social_media_website	                    =Column(String(255),nullable = True)
#     email_address                               =Column(String(255),nullable = True)
#     date_of_birth                               =Column(Date,nullable = True)	
#     contact_number                              =Column(String(255),nullable = True)
    
class sales_person(Base):

    __tablename__                              ="bde"
    id                                         = Column(Integer,autoincrement=True ,primary_key=True)
    name                                       = Column(String(255),nullable = True)
    designation                                 =Column(String(255),nullable = True)
    employee_id                                 =Column(String(255),primary_key=True)

# Create the table
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:ivania2019@localhost:5432/BDE_table"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:ivania2019@localhost:5432/XPB_Api_dev"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
Base.metadata.create_all(bind=engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

session.commit()

# Close the session
session.close()
