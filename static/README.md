Place your static assets here.

- Favicons: put `favicon.ico`, `favicon-32x32.png`, etc. at the repo root of `static/`.
- Images: create `static/images/` and add project images (logos, content images).

During development Django serves these when `DEBUG=True`.
Run `python manage.py collectstatic` for production to copy files into `STATIC_ROOT`.
