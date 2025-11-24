# 🚗 API Django REST Framework - Concessionnaire & Véhicules

API REST complète pour gérer des concessionnaires et leurs véhicules, avec authentification JWT.

## 📋 Prérequis

- Python 3.8+
- pip

## 🚀 Installation

1. **Cloner le projet** (ou se placer dans le répertoire)

2. **Créer un environnement virtuel** (recommandé) :
```bash
python -m venv venv
```

3. **Activer l'environnement virtuel** :
   - Windows : `venv\Scripts\activate`
   - Linux/Mac : `source venv/bin/activate`

4. **Installer les dépendances** :
```bash
pip install -r requirements.txt
```

5. **Créer les migrations** :
```bash
python manage.py makemigrations
```

6. **Appliquer les migrations** :
```bash
python manage.py migrate
```

7. **Créer un superutilisateur** (optionnel, pour l'admin Django) :
```bash
python manage.py createsuperuser
```

8. **Lancer le serveur** :
```bash
python manage.py runserver
```

Le serveur sera accessible sur `http://127.0.0.1:8000/`

9. **Accéder à la documentation interactive** :
   - **Swagger UI** : `http://127.0.0.1:8000/api/docs/`
   - **ReDoc** : `http://127.0.0.1:8000/api/redoc/`
   - **Schema OpenAPI** : `http://127.0.0.1:8000/api/schema/`

## 📚 Structure du projet

```
Django_Rest_Framework/
├── concessionnaire_api/      # Configuration du projet Django
│   ├── settings.py           # Configuration (DRF, JWT)
│   ├── urls.py               # URLs principales
│   └── ...
├── vehicules/                # Application principale
│   ├── models.py             # Modèles Concessionnaire & Véhicule
│   ├── serializers.py        # Serializers (siret exclu)
│   ├── views.py              # APIViews pour les endpoints
│   ├── urls.py               # URLs de l'API
│   └── ...
├── manage.py
├── requirements.txt
└── README.md
```

## 📖 Documentation Interactive (Swagger/OpenAPI)

L'API dispose d'une documentation interactive générée automatiquement avec **drf-spectacular**, similaire à FastAPI :

- **Swagger UI** : `http://127.0.0.1:8000/api/docs/` - Interface interactive pour tester les endpoints
- **ReDoc** : `http://127.0.0.1:8000/api/redoc/` - Documentation élégante et lisible
- **Schema OpenAPI** : `http://127.0.0.1:8000/api/schema/` - Schéma OpenAPI au format JSON/YAML

### Fonctionnalités de la documentation

La documentation permet de :
- ✅ Voir tous les endpoints disponibles avec leurs descriptions détaillées
- ✅ Tester les endpoints directement depuis le navigateur (comme FastAPI)
- ✅ Voir les schémas de requête/réponse avec exemples
- ✅ Comprendre les paramètres requis et les codes de réponse
- ✅ S'authentifier avec JWT directement dans l'interface Swagger

### Utilisation dans Swagger UI

1. Accédez à `http://127.0.0.1:8000/api/docs/`
2. Pour tester les endpoints protégés :
   - Cliquez sur le bouton **"Authorize"** en haut à droite
   - Entrez votre token JWT au format : `Bearer <votre_token_access>`
   - Cliquez sur **"Authorize"** puis **"Close"**
3. Vous pouvez maintenant tester tous les endpoints directement depuis l'interface !

## 🔐 Authentification JWT

L'API utilise JWT (JSON Web Tokens) pour l'authentification. Tous les endpoints (sauf création d'utilisateur et tokens) nécessitent un token valide.

### 1. Créer un utilisateur

**POST** `/api/users/`

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "motdepasse123"
}
```

**Réponse 201** :
```json
{
  "message": "Utilisateur créé avec succès.",
  "username": "john_doe",
  "email": "john@example.com"
}
```

### 2. Obtenir un token JWT

**POST** `/api/token/`

```json
{
  "username": "john_doe",
  "password": "motdepasse123"
}
```

**Réponse 200** :
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### 3. Rafraîchir le token

**POST** `/api/refresh_token/`

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Réponse 200** :
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

## 🌐 Endpoints de l'API

### ⚠️ Important
Tous les endpoints ci-dessous nécessitent un token JWT dans le header :
```
Authorization: Bearer <votre_token_access>
```

### Concessionnaires

#### 1. Lister tous les concessionnaires

**GET** `/api/concessionnaires/`

**Réponse 200** :
```json
[
  {
    "id": 1,
    "nom": "AutoPlus Paris"
  },
  {
    "id": 2,
    "nom": "MotoCenter Lyon"
  }
]
```

#### 2. Détails d'un concessionnaire

**GET** `/api/concessionnaires/<id>/`

**Réponse 200** :
```json
{
  "id": 1,
  "nom": "AutoPlus Paris"
}
```

**Note** : Le champ `siret` n'est jamais exposé dans l'API (ni en GET ni en POST/PUT/PATCH).

### Véhicules d'un concessionnaire

#### 3. Lister les véhicules d'un concessionnaire

**GET** `/api/concessionnaires/<id>/vehicules/`

**Réponse 200** :
```json
[
  {
    "id": 1,
    "type": "auto",
    "marque": "Peugeot",
    "chevaux": 120,
    "prix_ht": 25000.0,
    "concessionnaire": 1,
    "concessionnaire_nom": "AutoPlus Paris"
  },
  {
    "id": 2,
    "type": "moto",
    "marque": "Yamaha",
    "chevaux": 80,
    "prix_ht": 12000.0,
    "concessionnaire": 1,
    "concessionnaire_nom": "AutoPlus Paris"
  }
]
```

#### 4. Détails d'un véhicule

**GET** `/api/concessionnaires/<id>/vehicules/<vehicule_id>/`

**Réponse 200** :
```json
{
  "id": 1,
  "type": "auto",
  "marque": "Peugeot",
  "chevaux": 120,
  "prix_ht": 25000.0,
  "concessionnaire": 1,
  "concessionnaire_nom": "AutoPlus Paris"
}
```

## 🧪 Exemples de requêtes

### Avec cURL

#### 1. Créer un utilisateur
```bash
curl -X POST http://127.0.0.1:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "test123"}'
```

#### 2. Obtenir un token
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "test123"}'
```

#### 3. Lister les concessionnaires (avec token)
```bash
curl -X GET http://127.0.0.1:8000/api/concessionnaires/ \
  -H "Authorization: Bearer <votre_token_access>"
```

#### 4. Lister les véhicules d'un concessionnaire
```bash
curl -X GET http://127.0.0.1:8000/api/concessionnaires/1/vehicules/ \
  -H "Authorization: Bearer <votre_token_access>"
```

### Avec Postman / Bruno

1. **Créer une collection** "Concessionnaire API"

2. **Variables d'environnement** :
   - `base_url` : `http://127.0.0.1:8000`
   - `token` : (sera rempli après authentification)

3. **Requêtes** :
   - Créer utilisateur : `POST {{base_url}}/api/users/`
   - Obtenir token : `POST {{base_url}}/api/token/`
   - Lister concessionnaires : `GET {{base_url}}/api/concessionnaires/`
     - Header : `Authorization: Bearer {{token}}`
   - Détails concessionnaire : `GET {{base_url}}/api/concessionnaires/1/`
   - Liste véhicules : `GET {{base_url}}/api/concessionnaires/1/vehicules/`
   - Détails véhicule : `GET {{base_url}}/api/concessionnaires/1/vehicules/1/`

## 📝 Modèles de données

### Concessionnaire
- `id` : Integer (auto)
- `nom` : CharField(max_length=64)
- `siret` : CharField(max_length=14, unique) ⚠️ **Non exposé dans l'API**

### Véhicule
- `id` : Integer (auto)
- `type` : ChoiceField ("auto" ou "moto")
- `marque` : CharField(max_length=64)
- `chevaux` : IntegerField
- `prix_ht` : FloatField
- `concessionnaire` : ForeignKey vers Concessionnaire

## 🔧 Configuration

### JWT Settings
- **Access Token Lifetime** : 1 heure
- **Refresh Token Lifetime** : 7 jours
- **Rotation** : Activée

### Permissions
- Tous les endpoints (sauf création d'utilisateur et tokens) nécessitent une authentification JWT.

## 🛠️ Administration Django

Accéder à l'interface d'administration :
- URL : `http://127.0.0.1:8000/admin/`
- Utiliser les identifiants du superutilisateur créé avec `createsuperuser`

## 📌 Notes importantes

1. **Champ SIRET** : Le champ `siret` existe en base de données mais n'est **jamais exposé** dans l'API (ni en GET ni en POST/PUT/PATCH). C'est une exigence de sécurité.

2. **Authentification** : Tous les endpoints nécessitent un token JWT valide dans le header `Authorization: Bearer <token>`.

3. **Type de véhicule** : Les valeurs acceptées sont `"auto"` ou `"moto"`.

## 🐛 Dépannage

### Erreur "No module named 'rest_framework'"
```bash
pip install -r requirements.txt
```

### Erreur de migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### Erreur 401 Unauthorized
Vérifiez que vous avez inclus le token JWT dans le header :
```
Authorization: Bearer <votre_token>
```

## 📄 Licence

Ce projet est fourni à des fins éducatives.
