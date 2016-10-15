from wtforms import validators, StringField, SelectField, TextAreaField
from flask_wtf import FlaskForm
import requests
from config import CAPTCHA_KEY_SECRET, CSRF_SESSION_KEY


def handle_captcha_requests(response_from_form):
    url = 'https://www.google.com/recaptcha/api/siteverify?secret={0};response={1}'.format(
        CAPTCHA_KEY_SECRET, response_from_form
    )
    res = requests.post(url).json()
    return res['success']


class CallForPapers(FlaskForm):
    SECRET_KEY = CSRF_SESSION_KEY
    nome = StringField(
        'nome',
        [validators.DataRequired()],
        render_kw={
            "placeholder": "Nome",
            "class_": "form-control input-lg"
        })
    cognome = StringField(
        'cognome',
        [validators.DataRequired()],
        render_kw={
            "placeholder": "Cognome",
            "class_": "form-control input-lg"
        })
    email = StringField(
        'email',
        [validators.DataRequired(), validators.Email("Inserisci una mail valida")],
        render_kw={
            "placeholder": "Email",
            "class_": "form-control input-lg"
        })
    argomento = StringField(
        'argomento',
        [validators.DataRequired()],
        render_kw={
            "placeholder": "Titolo",
            "class_": "form-control input-lg"
        })
    abstract = TextAreaField(
        'abstract',
        [validators.DataRequired()],
        render_kw={
            "placeholder": "Riassunto",
            "class_": "form-control input-lg",
            "rows": 5
        })
    type_of_talk = SelectField(
        'Tipologia',
        choices=[('', '-- Tipo Intervento --'), ('talk', 'Talk'), ('tutorial', 'Tutorial'), ('workshop', 'Workshop')],
        render_kw={
            "class_": "form-control input-lg",
            "rows": 5
        }
    )
    durata = StringField(
        "Durata Prevista",
        render_kw={
            "placeholder": "Durata",
            "class_": "form-control input-lg",
            "rows": 5
        }
    )


class ContactForm(FlaskForm):
    """
    Classe form per invio mail dalla pagina dei contatti.

    Il submit e il reCAPTCHA li inserisco secchi nel template.
    """
    SECRET_KEY = CSRF_SESSION_KEY
    nome = StringField(
        'nome',
        [validators.DataRequired()],
        render_kw={
            "placeholder": "Nome",
            "class_": "form-control input-lg"
        })
    cognome = StringField(
        'cognome',
        [validators.DataRequired()],
        render_kw={
            "placeholder": "Cognome",
            "class_": "form-control input-lg"
        })
    email = StringField(
        'email',
        [validators.DataRequired(), validators.Email("Inserisci una mail valida")],
        render_kw={
            "placeholder": "Email",
            "class_": "form-control input-lg"
        })
    messaggio = TextAreaField(
        'messaggio',
        [validators.DataRequired()],
        render_kw={
            "placeholder": "Messaggio",
            "class_": "form-control input-lg",
            "rows": 5
        })
