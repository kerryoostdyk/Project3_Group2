from sqlalchemy import create_engine, text

import pandas as pd

# Define the SQLHelper Class
# PURPOSE: Deal with all of the database logic

class SQLHelper():

    # Initialize PARAMETERS/VARIABLES

    #################################################
    # Database Setup
    #################################################
    def __init__(self):
        self.engine = create_engine("sqlite:///UFO_data.sqlite")

    #################################################################

    def queryBarData(self, min_year,shape):
        # Create our session (link) from Python to the DB
        conn = self.engine.connect() # Raw SQL/Pandas

        # Define Query
        if shape == "all":
            query = text(f"""SELECT
                        Year as year,
                        count (*) as num_ufosighting
                    FROM
                        UFO_data
                    WHERE
                        Year >= {min_year}
                    GROUP BY
                        Year
                    ORDER BY
                        Year asc;""")
        else:
        # When shape is specified, filter by UFO_shape
            query = text(f"""SELECT
                        Year as year,
                        count (*)as num_ufosighting
                    FROM
                        UFO_data
                    WHERE
                        Year >= {min_year} AND UFO_shape = :shape
                    GROUP BY
                        Year
                    ORDER BY
                        Year asc;""")
        
    # Execute the query with parameter for UFO shape
        df = pd.read_sql(query, con=conn, params={"shape": shape})

        # Close the connection
        conn.close()
        return(df)

    def queryTableData(self, min_year,shape):
        # Create our session (link) from Python to the DB
        conn = self.engine.connect() # Raw SQL/Pandas
        print(shape)
        # Define Query
        if shape != "all":  
            query = text("""SELECT
                        Year as year,
                        Season as season,
                        Country as country,
                        UFO_shape as UFO_shape,
                        Latitude as latitude,
                        Longitude as longitude
                    FROM
                        UFO_data
                    WHERE
                        Year >= :min_year AND UFO_shape = :shape
                    ORDER BY
                        Year asc
                    limit 200  ;""")
            df = pd.read_sql(query, con=conn,params={"min_year": min_year,"shape": shape})  # Pass the shape as a parameter
        else:
            query = text("""SELECT
                        Year as year,
                        Season as season,
                        Country as country,
                        UFO_shape as UFO_shape,
                        Latitude as latitude,
                        Longitude as longitude
                    FROM
                        UFO_data
                    WHERE
                        Year >= :min_year
                    ORDER BY
                        Year asc
                    limit 200 ;""")
            df = pd.read_sql(query, con=conn,params={"min_year": min_year})  # No additional parameters

        # Close the connection
        conn.close()
        return(df)

    def queryMapData(self, min_year):
        # Create our session (link) from Python to the DB
        conn = self.engine.connect() # Raw SQL/Pandas

        # Define Query
        query = text(f"""SELECT
                    Year as year,
                    Season as season,
                    Hour as hour,
                    Region as region,
                    Country as country,
                    UFO_shape as UFO_shape,
                    Latitude as latitude,
                    Longitude as longitude
                FROM
                    UFO_data
                WHERE
                    Year >= {min_year}
                ORDER BY
                    Year asc;""")
        df = pd.read_sql(query, con=conn)

        # Close the connection
        conn.close()
        return(df)
    
    def queryScatterData(self,min_year,shape):
        # Create our session (link) from Python to the DB
        conn = self.engine.connect() # Raw SQL/Pandas

        # Define Query
        if shape == "all":
            query = text(f"""SELECT
                        Country as country,
                        count (*) as num_ufosighting
                    FROM
                       UFO_data
                    WHERE
                        Year >= {min_year}
                    GROUP BY
                        Country,Year
                    ORDER BY
                        Year asc;""")
        else:
        # When shape is specified, filter by UFO_shape
            query = text(f"""SELECT
                        Country as country,
                        count (*) as num_ufosighting
                    FROM
                        UFO_data
                    WHERE
                        Year >= {min_year} AND UFO_shape = :shape
                    GROUP BY
                        Country,Year
                    ORDER BY
                        Year asc;""")
            
        df = pd.read_sql(query, con=conn, params={"shape": shape})
        # Close the connection
        conn.close()
        return(df)
    
    def queryBubbleData(self,min_year,shape):
        # Create our session (link) from Python to the DB
        conn = self.engine.connect() # Raw SQL/Pandas

        # Define Query
        if shape == "all":
            query = text(f"""SELECT
                        Year as year,
                        Hour as Hour,
                        Estimated_Encounter_Duration_Minutes as Estimated_Encounter_Duration_Minutes
                    FROM
                       UFO_data
                    WHERE
                        Year >= {min_year}
                    GROUP BY
                        Year
                    ORDER BY
                        Year asc;""")
        else:
        # When shape is specified, filter by UFO_shape
            query = text(f"""SELECT
                        Year as year,
                        Hour as Hour,
                        Estimated_Encounter_Duration_Minutes as Estimated_Encounter_Duration_Minutes
                    FROM
                        UFO_data
                    WHERE
                        Year >= {min_year} AND UFO_shape = :shape
                    GROUP BY
                        Year
                    ORDER BY
                        Year asc;""")
            
        df = pd.read_sql(query, con=conn, params={"shape": shape})
        # Close the connection
        conn.close()
        return(df)
    
    def queryDonutData(self, min_year,shape):
        # Create our session (link) from Python to the DB
        conn = self.engine.connect() # Raw SQL/Pandas

        # Define Query
        if shape == "all":
            query = text(f"""SELECT
                        Season as season,
                        count (*) as num_ufosighting
                    FROM
                        UFO_data
                    WHERE
                        Year >= {min_year}
                    GROUP BY
                        Season
                    ORDER BY
                        Year asc;""")
        else:
        # When shape is specified, filter by UFO_shape
            query = text(f"""SELECT
                        Season as season,
                        count (*)as num_ufosighting
                    FROM
                        UFO_data
                    WHERE
                        Year >= {min_year} AND UFO_shape = :shape
                    GROUP BY
                        Season
                    ORDER BY
                        Year asc;""")
        
    # Execute the query with parameter for UFO shape
        df = pd.read_sql(query, con=conn, params={"shape": shape})

        # Close the connection
        conn.close()
        return(df)