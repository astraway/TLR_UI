from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import current_user, login_required
from tlr_ui import db
from tlr_ui.models import QuoteCreation
from tlr_ui.add_repair.forms import CreateQuoteForm
from tlr_ui.users.picture_handler import add_profile_pic

quoting = Blueprint('createquote',__name__)

# register
@quoting.route('/create',methods=['GET','POST'])
@login_required
def create_quote():
    form = CreateQuoteForm()

    if form.validate_on_submit():
        quote_request = QuoteCreation(
                    user_id=current_user.id,
                    BEGEOID=form.BEGEOID.data,
                  CAMPAIGN_DUE_DATE=form.CAMPAIGN_DUE_DATE.data,
                  CAMPAIGN_TYPE=form.CAMPAIGN_TYPE.data,
                  CCOID=form.CCOID.data,
                  DATA_SOURCE_TYPE=form.DATA_SOURCE_TYPE.data,
                  DEFAULT_DAYS_FUTURE=form.DEFAULT_DAYS_FUTURE.data
                  )

        db.session.add(quote_request)
        db.session.commit()
        flash('Your Quotes will begin to process soon...')
        return redirect(url_for('core.index'))

    return render_template('create_quote.html',form=form)

@quoting.route('/<int:quote_id>')
@login_required
def quote(quote_id):
    quote = QuoteCreation.query.get_or_404(quote_id)
    return render_template('quote.html', user_id=QuoteCreation.user_id,
                    BEGEOID=QuoteCreation.BEGEOID,
                  CAMPAIGN_DUE_DATE=QuoteCreation.CAMPAIGN_DUE_DATE,
                  CAMPAIGN_TYPE=QuoteCreation.CAMPAIGN_TYPE,
                  CCOID=QuoteCreation.CCOID,
                  DATA_SOURCE_TYPE=QuoteCreation.DATA_SOURCE_TYPE,
                  DEFAULT_DAYS_FUTURE=QuoteCreation.DEFAULT_DAYS_FUTURE,
                    THIS_QUOTE = quote )