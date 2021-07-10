
def create_app(options = None):
  from app.config import get_config
  from app.models import db, ListItem
  from flask import Flask, request, jsonify


  app = Flask(__name__)
  config = get_config(options)
  app.config.from_object(config)
  db.init_app(app)

  # Resets the database
  @app.route('/reset_db')
  def reset_db():
    try:
      db.drop_all()
      db.create_all()
      return 'OK'
    except Exception as e:
      return str(e)


  # Adds an item to the list, returns the created item
  @app.route('/api/item', methods=['POST'])
  def create():
    try:
      item = ListItem(text=request.json.get('text'))
      db.session.add(item)
      db.session.commit()
      return jsonify(item)
    except Exception as e:
      return str(e)


  # Returns item with id <id>, if exists, otherwise returns {}
  @app.route('/api/item/<id>', methods=['GET'])
  def get(id):
    try:
      item = ListItem.query.get(id)
      return jsonify(item) if item else {}
    except:
      return {}


  # Returns all items in the list
  @app.route('/api/item', methods=['GET'])
  def get_all():
    try:
      return jsonify(ListItem.query.all())
    except:
      return {}


  # Updates item with id <id> based on the fields input fields,
  # on success returns the updated item, otherwise {}
  @app.route('/api/item/<id>', methods=['PUT'])
  def update(id):
    try:
      item = ListItem.query.get(id)
      for attr, value in request.json.items():
        setattr(item, attr, value)
      db.session.commit()
      return jsonify(item)
    except:
      return {}


  # Deletes item with id <id> from the list, onsuccess returns the <id>,
  # otherwise returns -1
  @app.route('/api/item/<id>', methods=['DELETE'])
  def delete(id):
    try:
      item = ListItem.query.get(id)
      db.session.delete(item)
      db.session.commit()
      return str(id)
    except:
      return '-1'

  return app
