from app.funcao import funcao_ola_turma

def teste_ola_turma_retorna_ola_todos():
    saida = funcao_ola_turma()
    gabarito = "ola todos"
    assert saida == gabarito
