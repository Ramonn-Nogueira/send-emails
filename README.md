<div>
<h1>Send-emails.py</h1>
<p>Um protótipo de programa em python que envia e-mails listados em um arquivo .csv</p>
</div>
<h1>Bibliotecas</h1>

<div>
<h2>Email.message</h2>
<p>O analisador sintático pega a versão serializada de uma mensagem de e-mail (um fluxo de bytes) e a converte em uma árvore de objetos EmailMessage. O gerador pega um EmailMessage e o transforma novamente em um fluxo de bytes serializado. (O analisador sintático e o gerador também lidam com fluxos de caracteres de texto, mas esse uso é desencorajado, pois é muito fácil terminar com mensagens que não são válidas de uma maneira ou de outra.)</p>
<code>import email.message</code>
</div>

<div>
<h2>CSV</h2>
<p>O módulo csv implementa classes para ler e gravar dados tabulares no formato CSV. Ele permite que os programadores digam “escreva esses dados no formato preferido pelo Excel” ou “leia os dados desse arquivo gerado pelo Excel”, sem conhecer os detalhes precisos do formato CSV usado pelo Excel. Os programadores também podem descrever os formatos CSV entendidos por outros aplicativos ou definir seus próprios formatos CSV para fins especiais.</p>
<code>import csv</code>
</div>


<div>
<h2>Smtplib</h2>
<p>Módulo usado para envios de e-mails</p>
<code>import smtplib
</code>
</div>

<div><h2>Print do código</h2>
<img src='readme-mail.png'></div>
