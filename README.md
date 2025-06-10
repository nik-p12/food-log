# 🍽️ Projet Backend – INF222 : Système de Recommandation Alimentaire

Ce projet a été réalisé dans le cadre du cours **INF222 (Backend Development Practice)**, dispensé à l’Université de Yaoundé I.  
Il vise à permettre aux étudiants de se familiariser avec les techniques et outils de développement backend à travers une problématique concrète de **gestion nutritionnelle et de recommandation alimentaire**.

---

## 🚀 Fonctionnalités principales

- Création et gestion des utilisateurs
- Suivi des repas et des aliments consommés
- Enregistrement des allergies et problèmes de santé
- Association entre aliments et réactions indésirables
- Système de recommandation intelligente d'aliments
- Organisation des aliments par **catégories nutritionnelles**

---

## 🏗️ Installation

```bash
git clone https://github.com/ton-user/backend-alimentaire.git
cd backend-alimentaire
python -m venv env
source env/bin/activate  # ou `env\Scripts\activate` sur Windows
pip install -r requirements.txt
````

### ⚙️ Lancement du serveur

```bash
export FLASK_APP=app.py  # sur Windows : set FLASK_APP=app.py
flask run
```

Serveur disponible à : `http://127.0.0.1:5000`

---

## 📚 Endpoints principaux

### 👤 Utilisateurs (`User`)

| Méthode  | URL               | Description                                     |
| -------- | ----------------- | ----------------------------------------------- |
| `GET`    | `/api/users`      | Liste tous les utilisateurs                     |
| `GET`    | `/api/users/<id>` | Détail d’un utilisateur                         |
| `POST`   | `/api/users`      | Crée un nouvel utilisateur                      |
| `PATCH`  | `/api/users/<id>` | Modifie un ou plusieurs champs d’un utilisateur |
| `DELETE` | `/api/users/<id>` | Supprime un utilisateur                         |

---

### 🥘 Repas (`Meal`) & 🍽️ Aliments consommés (`MealFood`)

#### Repas – `/api/meals`

| Méthode  | Description                               |
| -------- | ----------------------------------------- |
| `GET`    | Liste ou détail des repas                 |
| `POST`   | Crée un repas                             |
| `PATCH`  | Modifie un ou plusieurs champs d’un repas |
| `DELETE` | Supprime un repas                         |

#### Aliments d’un repas – `/api/meal_foods`

| Méthode  | Description                                               |
| -------- | --------------------------------------------------------- |
| `GET`    | Liste ou détail des aliments d’un repas                   |
| `POST`   | Associe un aliment à un repas                             |
| `PATCH`  | Modifie un ou plusieurs champs d’une entrée repas-aliment |
| `DELETE` | Supprime l’entrée d’un aliment dans un repas              |

---

### 🍎 Aliments (`Food`)

| Méthode  | URL                                         |
| -------- | ------------------------------------------- |
| `GET`    | `/api/foods` ou `/api/foods/<id>`           |
| `POST`   | Crée un aliment                             |
| `PATCH`  | Modifie un ou plusieurs champs d’un aliment |
| `DELETE` | Supprime un aliment                         |

#### Exemple de payload pour POST

```json
{
  "name": "Pomme",
  "description": "Fruit rouge ou vert",
  "calories": 52,
  "category_id": 1
}
```

---

### 🧠 Problèmes de santé (`HealthIssue`)

| Méthode  | URL                                                   |
| -------- | ----------------------------------------------------- |
| `GET`    | `/api/health_issues` ou `/api/health_issues/<id>`     |
| `POST`   | Crée un problème de santé                             |
| `PATCH`  | Modifie un ou plusieurs champs d’un problème de santé |
| `DELETE` | Supprime un problème de santé                         |

---

### ⚠️ Réactions de santé (`HealthReaction`)

Permet d’enregistrer les réactions à certains repas.

| Méthode  | URL                                           |
| -------- | --------------------------------------------- |
| `GET`    | `/api/health_reactions`                       |
| `POST`   | Crée une réaction                             |
| `PATCH`  | Modifie un ou plusieurs champs d’une réaction |
| `DELETE` | Supprime une réaction                         |

---

### 🌾 Allergies (`Allergy`)

| Méthode  | URL                                           |
| -------- | --------------------------------------------- |
| `GET`    | `/api/allergies`                              |
| `POST`   | Crée une allergie                             |
| `PATCH`  | Modifie un ou plusieurs champs d’une allergie |
| `DELETE` | Supprime une allergie                         |

---

### 🗂️ Catégories (`Category`)

| Méthode  | URL                                            |
| -------- | ---------------------------------------------- |
| `GET`    | `/api/categories`                              |
| `POST`   | Crée une catégorie                             |
| `PATCH`  | Modifie un ou plusieurs champs d’une catégorie |
| `DELETE` | Supprime une catégorie                         |

---

### 🤖 Recommandation d’aliments (`FoodRecommendation`)

| Méthode | URL                                |
| ------- | ---------------------------------- |
| `GET`   | `/users/<user_id>/recommendations` |

Retourne les aliments **recommandés** pour un utilisateur, en excluant ceux :

* associés à une allergie,
* liés à une réaction grave passée,
* incompatibles avec ses problèmes de santé (ex. : diabète et sucre).

---

## 🧪 Exemple de réponse – Recommandation

```json
[
  {
    "id": 2,
    "name": "Riz complet",
    "calories": 110,
    "description": "Source de fibres, bon pour la digestion"
  }
]
```

---

## 🧰 Stack technique

* **Python 3 / Flask / Flask-RESTful**
* **SQLAlchemy ORM**
* **SQLite** (facile à remplacer par PostgreSQL, MySQL, etc.)
* Architecture modulaire et RESTful

---

## 📦 Peuplement automatique (dev)

Dans `app.py`, décommente `populate()` pour insérer des données de test :

```python
# populate()
```

---

## 📄 Licence

Projet libre – Utilisation académique ou personnelle.

---

## 🙌 Contributeurs

Projet développé dans le cadre d’un cours universitaire de backend – **INF222**.
