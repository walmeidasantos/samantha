from mensagemAdapterApi import IAGenerativa

def resumidor_de_historico(historico):

    messages=f"""
            Resumir progressivamente as linhas de conversa fornecidas, 
            acrescentando ao resumo anterior e retornando um novo resumo. 
            Não apague nenhum assunto da conversa. 
            Se não houver resumo, apenas continue a conversa normalmente.

            ## EXEMPLO:
            O usuario pergunta o que a IA pensa sobre a inteligência artificial. 
            A IA acredita que a inteligência artificial é uma força para o bem.
            Usuário: Por que você acha que a inteligência artificial é uma força para o bem?
            IA: Porque a inteligência artificial ajudará os humanos a alcançarem seu pleno 
            potencial.

            ### Novo resumo:
            O usuario questiona a razão pela qual a IA considera a inteligência artificial 
            uma força para o bem, e a IA responde que é porque a inteligência artificial 
            ajudará os humanos a atingirem seu pleno potencial.

            ## FIM DO EXEMPLO
            
            Resumo atual:
            {historico}

            Novo resumo:"""
    resposta_resumidor = IAGenerativa.gerar_texto_personalizado(self=IAGenerativa,prompt=messages)
    return resposta_resumidor

def criando_resumo(historico):
    resumo = resumidor_de_historico(historico=historico)
    return resumo