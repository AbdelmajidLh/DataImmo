import mysql.connector
from mysql.connector import Error

# Configuration de la connexion à la base de données MySQL
db_config = {
    'host': 'localhost',
    'user': 'votre_utilisateur',
    'password': 'votre_mot_de_passe'
}

# Nom de la base de données
db_name = 'dataimmo'

# Création de la base de données
def create_database():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print("Base de données créée avec succès!")
    except Error as e:
        print("Erreur lors de la création de la base de données:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Création des tables
def create_tables():
    try:
        connection = mysql.connector.connect(database=db_name, **db_config)
        cursor = connection.cursor()

        # Création de la table T_COMMUNE
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS T_COMMUNE (
                commune_id INT NOT NULL,
                code_departement VARCHAR(20) NOT NULL,
                commune VARCHAR(70) NOT NULL,
                PRIMARY KEY (commune_id)
            )
        """)

        # Création de la table T_LOCAL
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS T_LOCAL (
                local_id INT AUTO_INCREMENT NOT NULL,
                type_local VARCHAR(50) NOT NULL,
                PRIMARY KEY (local_id)
            )
        """)

        # Création de la table T_BIEN
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS T_BIEN (
                bien_id INT NOT NULL,
                date_mutation DATETIME NOT NULL,
                nature_mutation VARCHAR(70) NOT NULL,
                valeur_fonciere DECIMAL(10,2),
                surface_carrez DECIMAL(10,2) NOT NULL,
                nombre_pieces_principales INT NOT NULL,
                commune_id INT NOT NULL,
                local_id INT NOT NULL,
                PRIMARY KEY (bien_id)
            )
        """)

        print("Tables créées avec succès!")
    except Error as e:
        print("Erreur lors de la création des tables:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Insertion des données à partir de fichiers CSV
def insert_data_from_csv():
    try:
        connection = mysql.connector.connect(database=db_name, **db_config)
        cursor = connection.cursor()

        # Insertion des données dans T_COMMUNE depuis le fichier CSV commune.csv
        with open('commune.csv', 'r') as csv_file:
            next(csv_file)  # Skip header
            for line in csv_file:
                values = line.strip().split(',')
                cursor.execute("INSERT INTO T_COMMUNE (commune_id, code_departement, commune) VALUES (%s, %s, %s)", values)

        # Insertion des données dans T_LOCAL depuis le fichier CSV local.csv
        with open('local.csv', 'r') as csv_file:
            next(csv_file)  # Skip header
            for line in csv_file:
                values = line.strip().split(',')
                cursor.execute("INSERT INTO T_LOCAL (local_id, type_local) VALUES (DEFAULT, %s)", (values[0],))

        # Insertion des données dans T_BIEN depuis le fichier CSV bien.csv
        with open('bien.csv', 'r') as csv_file:
            next(csv_file)  # Skip header
            for line in csv_file:
                values = line.strip().split(',')
                cursor.execute("INSERT INTO T_BIEN (bien_id, date_mutation, nature_mutation, valeur_fonciere, surface_carrez, nombre_pieces_principales, commune_id, local_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", values)

        connection.commit()
        print("Données insérées avec succès!")
    except Error as e:
        print("Erreur lors de l'insertion des données:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Génération d'un script SQL pour des requêtes
def generate_sql_script():
    sql_script = """
    -- Requête 1 : Exemple de requête
    SELECT commune, ROUND(AVG(valeur_fonciere), 2) AS Moyenne
    FROM T_BIEN
    INNER JOIN T_COMMUNE USING (commune_id)
    GROUP BY commune
    ORDER BY Moyenne DESC
    LIMIT 20;
    
    -- Requête 2 : Autre exemple de requête
    SELECT code_departement, COUNT(*) AS Nombre_Appartements
    FROM T_BIEN
    INNER JOIN T_LOCAL USING (local_id)
    INNER JOIN T_COMMUNE USING (commune_id)
    WHERE type_local = 'Appartement'
    GROUP BY code_departement;
    """

    with open('queries.sql', 'w') as sql_file:
        sql_file.write(sql_script)

    print("Script SQL généré avec succès!")

# Appel des fonctions pour créer la base, les tables, insérer les données et générer le script SQL
create_database()
create_tables()
insert_data_from_csv()
generate_sql_script()
