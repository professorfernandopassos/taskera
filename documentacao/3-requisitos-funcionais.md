# Requisitos Funcionais

1. Tela de registro de usuário contendo entrada para nome, email e senha com uma interação para envio dos dados fornecidos, exibição dos termos de uso do software e a interação de aceitação desses termos.
2. Caso o registro falhe, um aviso será apresentado na tela de registro contendo o motivo da falha.
3. Após o registro do novo usuário, haverá um redirecionamento para a tela de autenticação do usuário.
4. Tela de autenticação do usuário contendo entrada para email e senha com uma interação para envio dos dados fornecidos assim como uma interação que redireciona o usuário para uma tela de troca de senha. 
5. Caso a autenticação falhe, um aviso será apresentado na tela de autenticação contendo o motivo da falha.
6. Caso o usuário tenha esquecido sua senha, poderá acessar a tela de troca de senha que conterá uma entrada para o email do usuário e uma interação de envio do dado. 
   1. Nesse caso, um email será enviado contendo um link para uma nova tela que possibilitará a troca da senha apresentando uma entrada para a nova senha e outra entrada para a repetição da senha. Após o usuário fornacer senhas válidas, a senha atual será alterada.
7. Após a autenticação, o usuário será direcionado para a tela da lista de tarefas onde haverá, além dessa lista: 
   1. Inclusão da tarefa digitada.
   2. Marcação de tarefa concluída em cada item da lista.
   3. Alteração do texto de uma tarefa preexistente.
   4. Exclusão de uma tarefa em cada item da lista.
   5. Direcionamento para a tela de saída do sistema.
8. Tela de saída do sistema com interação específica e redirecionamento posterior à saída para a tela de autenticação.