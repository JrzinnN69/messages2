from flask import jsonify, request
from .models import Mensagem
from . import db

def criar_mensagem():
    data = request.get_json()
    nova = Mensagem(conteudo=data['conteudo'])
    db.session.add(nova)
    db.session.commit()
    return jsonify({'id': nova.id, 'conteudo': nova.conteudo}), 201

def listar_mensagens():
    mensagens = Mensagem.query.all()
    return jsonify([{'id': m.id, 'conteudo': m.conteudo} for m in mensagens])

def obter_mensagem(id):
    mensagem = Mensagem.query.get_or_404(id)
    return jsonify({'id': mensagem.id, 'conteudo': mensagem.conteudo})

def atualizar_mensagem(id):
    mensagem = Mensagem.query.get_or_404(id)
    data = request.get_json()
    mensagem.conteudo = data['conteudo']
    db.session.commit()
    return jsonify({'id': mensagem.id, 'conteudo': mensagem.conteudo})

def deletar_mensagem(id):
    mensagem = Mensagem.query.get_or_404(id)
    db.session.delete(mensagem)
    db.session.commit()
    return jsonify({'mensagem': 'Mensagem deletada'})
