from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.forms.models import model_to_dict
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Board
from adverts.models import Advert

from .forms import BoardForm
from adverts.views import get_ads

def notice_boards(request):
    """ Generate Notice Boards Page """
    return render(request, 'notice_boards.html', {'active_boards': Board.objects.all()})

def display_single_board(request, board_pk):
    """ Render a single notice board page """
    notice_board = get_object_or_404(Board, pk=board_pk)
    adverts = Advert.objects.filter(boards=notice_board)
    return render(request, 'single_notice_board.html', {'notice_board':notice_board, 'adverts':adverts})

def get_notice_board(board_pk):
    """ Generate html for requested notice board with all its adverts """
    # Get the details of the board or raise a 404 if it doesn't exist
    try:
        board_meta = Board.objects.get(pk=board_pk)
    except:
        raise Http404("Notice board not found")
    # Get the adverts for this board
    board_ads = get_ads(board_pk)
    # Generate the notice board html
    notice_board = render_to_string('notice_board.html',
        {
            'board_meta' : board_meta,
            'adverts' : board_ads
        })
    return notice_board

def set_favourite_board(request, board_pk, set_unset=False):
    """ Set or unset favourite board pk in user profile or local cookie and reload page """
    if request.user.is_authenticated:
        # Set or unset favourite board in user profile
        if set_unset:
            # Set favourite in PPUser profile
            request.user.ppuser.favourite_board = Board.objects.get(pk=board_pk)           
            request.user.ppuser.save()
        else:
            # Unset favourite in PPUser profile
            request.user.ppuser.favourite_board = None
            request.user.ppuser.save()
    else:        
        # Set or unset favourite board in local cookie
        if set_unset:
            request.session['favourite_board'] = board_pk
        else:
            if request.session.__contains__('favourite_board'):
                del request.session['favourite_board']

    return redirect('display_single_board', board_pk = board_pk)

@login_required
def create_notice_board(request):
    """ Create a notice board from list of available postcode districts or display form to do so """
    
    if request.method == "POST":
        # If for data posted, check and save
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board_form.save()
            return redirect('boards')
        else:
            return render(request, 'create_notice_board.html', {'page_title':'Create Notice Board', 'board_form':board_form})
    
    # Or just create a blank form
    board_form = BoardForm()
    return render(request, 'create_notice_board.html', {'page_title':'Create Notice Board', 'board_form':board_form})