from flask import jsonify, request
from .models import Mensagem
from . import db

# Criar uma nova mensagem
def criar_mensagem():
    try:
        data = request.get_json()

        if not data or 'conteudo' not in data:
            return jsonify({'erro': 'Campo "conteudo" é obrigatório.'}), 400

        conteudo = data['conteudo'].strip()
        if not conteudo:
            return jsonify({'erro': 'O conteúdo da mensagem não pode estar vazio.'}), 400

        nova = Mensagem(conteudo=conteudo)
        db.session.add(nova)
        db.session.commit()

        return jsonify({'id': nova.id, 'conteudo': nova.conteudo}), 201

    except Exception as e:
        return jsonify({'erro': 'Erro ao criar mensagem.', 'detalhes': str(e)}), 500


# Listar todas as mensagens
def listar_mensagens():
    try:
        mensagens = Mensagem.query.all()
        return jsonify([{'id': m.id, 'conteudo': m.conteudo} for m in mensagens])
    except Exception as e:
        return jsonify({'erro': 'Erro ao listar mensagens.', 'detalhes': str(e)}), 500


# Obter uma mensagem específica
def obter_mensagem(id):
    try:
        mensagem = Mensagem.query.get(id)
        if mensagem is None:
            return jsonify({'erro': f'Mensagem com ID {id} não encontrada.'}), 404

        return jsonify({'id': mensagem.id, 'conteudo': mensagem.conteudo})
    except Exception as e:
        return jsonify({'erro': 'Erro ao obter mensagem.', 'detalhes': str(e)}), 500


# Atualizar o conteúdo de uma mensagem
def atualizar_mensagem(id):
    try:
        mensagem = Mensagem.query.get(id)
        if mensagem is None:
            return jsonify({'erro': f'Mensagem com ID {id} não encontrada.'}), 404

        data = request.get_json()
        if not data or 'conteudo' not in data:
            return jsonify({'erro': 'Campo "conteudo" é obrigatório.'}), 400

        conteudo = data['conteudo'].strip()
        if not conteudo:
            return jsonify({'erro': 'O conteúdo da mensagem não pode estar vazio.'}), 400

        mensagem.conteudo = conteudo
        db.session.commit()

        return jsonify({'id': mensagem.id, 'conteudo': mensagem.conteudo})

    except Exception as e:
        return jsonify({'erro': 'Erro ao atualizar mensagem.', 'detalhes': str(e)}), 500


# Deletar uma mensagem
def deletar_mensagem(id):
    try:
        mensagem = Mensagem.query.get(id)
        if mensagem is None:
            return jsonify({'erro': f'Mensagem com ID {id} não encontrada.'}), 404

        db.session.delete(mensagem)
        db.session.commit()
        return jsonify({'mensagem': 'Mensagem deletada com sucesso.'})

    except Exception as e:
        return jsonify({'erro': 'Erro ao deletar mensagem.', 'detalhes': str(e)}), 500
