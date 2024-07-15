from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory='templates')

class Comments(BaseModel):
    name: str
    comment: str
    type: str

words = [
         ]



@app.post('/')
def comment_post(request: Request, username: str = Form(None), comment: str = Form(None), type: str = Form(None)):
    u = username
    c = comment

    if not u:
        u =  'anonymus'
    if not c:
        c = '.'
    words.append(Comments(name=u, comment=c, type=type))
    print(words)
    return RedirectResponse('/', status_code=303)


@app.get('/', response_class=HTMLResponse)
def main(request: Request, per: int = 5, page: int = 1):
    step = per*page
    length = len(words)
    per_page = words[step-per:step]
    return templates.TemplateResponse('index.html', {'request': request, 'comments': per_page, 'len':length, 'page_html':page})




