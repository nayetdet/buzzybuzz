# buzzybuzz

Configure um `.env` baseado em `.env.example`.

Para listar a inbox:

```bash
uv run python -m buzzybuzz inbox
```

Para enviar email:

```bash
uv run python -m buzzybuzz send --to destino@example.com --subject "Teste" --body "Mensagem"
```

Com Gmail, use uma senha de app no campo `PASSWORD`; a senha normal da conta geralmente nao funciona em IMAP/SMTP.
