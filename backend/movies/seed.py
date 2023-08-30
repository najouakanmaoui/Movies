import psycopg2
import os
# Database configuration
db_config = {
    "dbname": "postgres",
    "user": "root",
    "password": "postgres",
    "host": "postgres",  
    "port": "5432",
}

# SQL statements
sql_statements = """
   
INSERT INTO public.auth_user ("password",last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined) VALUES
	 ('pbkdf2_sha256$600000$iCod36JjlB4Qsp378VAKGa$+t2rNTpvk5wac78SIQ33jPFRrAfxhzlgyZp0vuJ1Qy0=','2023-08-30 14:51:09.298813+01',true,'najoua','','','najoua@example.com',true,true,'2023-08-30 14:49:33.129919+01');
INSERT INTO public.reviews_actor (first_name,last_name) VALUES
	 ('najoua','kanmaoui'),
	 ('Viola','Davis'),
	 ('Will','Smith'),
	 ('Sandra','Bullock'),
	 ('Jennifer','Lawrence'),
	 ('David','shwimmer'),
	 ('matt','le blanc'),
	 ('Jennifer','aniston'),
	 ('Kristen','Bell');
INSERT INTO public.reviews_movie (title,description) VALUES
	 ('test title','test desc'),
	 ('Hunger games','best movie'),
	 ('Pursuit of happiness','best movie'),
	 ('Fences','best movie'),
	 ('The Unforgivable','best movie'),
	 ('friends','best tv show'),
	 ('Best place','good tv show');
INSERT INTO public.reviews_movie_actors (movie_id,actor_id) VALUES
	 (1,1),
	 (2,5),
	 (3,3),
	 (4,2),
	 (5,4),
	 (6,8),
	 (6,6),
	 (6,7),
	 (7,9);
INSERT INTO public.reviews_review (grade,movie_id) VALUES
	 (4,1),
	 (3,1),
	 (5,1),
	 (3,1),
	 (1,1),
	 (1,1),
	 (1,1),
	 (1,1),
	 (1,1),
	 (1,1),
	 (1,1),
	 (1,1),
	 (4,1);

"""

def seed_database():
    
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()
        statements = sql_statements.strip().split(";")
        for statement in statements:
            if statement.strip():
                cursor.execute(statement)

        connection.commit()
        print("Database seeded successfully.")

    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    seed_database()
