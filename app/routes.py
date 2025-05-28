from flask import Blueprint
from .controllers import (
    criar_mensagem,
    listar_mensagens,
    obter_mensagem,
    atualizar_mensagem,
    deletar_mensagem
)

mensagens_bp = Blueprint('mensagens', __name__)

mensagens_bp.route('/mensagens', methods=['POST'])(criar_mensagem)
mensagens_bp.route('/mensagens', methods=['GET'])(listar_mensagens)
mensagens_bp.route('/mensagens/<int:id>', methods=['GET'])(obter_mensagem)
mensagens_bp.route('/mensagens/<int:id>', methods=['PUT'])(atualizar_mensagem)
mensagens_bp.route('/mensagens/<int:id>', methods=['DELETE'])(deletar_mensagem)
