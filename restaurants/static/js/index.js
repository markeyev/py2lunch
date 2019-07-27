const TEMPLATE = `<div class="card">
    <div class="card-body">
        <div class="flex pad-box">
            <div style="flex: 1">{{REST_NAME}}</div>
            <div class="progress" style="flex: 1">
                <div class="progress-bar" role="progressbar" style="width: {{REST_OVERALL_RATING}}%" aria-valuenow="{{REST_OVERALL_RATING}}" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
            <a style="display: {{BUTTON_STYLE}}" data="{{ID}}" href="#" class="btn btn-primary">✓</a>
        </div>
    </div>
</div>`;

let global_data = null;

$(document).ready(() => {
    $('#main_container').click(event => {
        if(event.target.tagName.toLowerCase() === 'a') {
            const id = event.target.getAttribute('data');
            $.get('/go/' + id, () => {
                global_data.voted = true;
                global_data.restaurants.forEach(restaurant => {
                    if(restaurant.id === Number(id)) {
                        restaurant.rating++;
                    }
                });
                parse_data(global_data);
            });
        }
    });

    let promise = new Promise(function(resolve, reject) {
        if(window.mock_data !== undefined) {
            resolve(mock_data);
        } else {
            $.getJSON('/restaurants', (data) => {
                resolve(data);
            });
        }
    });
    promise.then(parse_data);
});

function parse_data(restaurants_data) {
    global_data = restaurants_data;
    $('#main_container').html('');
    let restaurants = restaurants_data.restaurants;
    let max = -Infinity;
    restaurants.forEach(restaurant => {
        max = Math.max(max, restaurant.rating);
    });
    restaurants.sort((a, b) => {
        return b.rating / max - a.rating / max;
    });
    restaurants.forEach(restaurant => {
        let template = TEMPLATE
            .replace(/{{ID}}/g, restaurant.id)
            .replace(/{{REST_NAME}}/g, restaurant.name)
            .replace(/{{BUTTON_STYLE}}/g, restaurants_data.voted ? 'none' : 'block')
            .replace(/{{REST_OVERALL_RATING}}/g, (restaurant.rating / max) * 100);
        $('#main_container').append(template);
    });
}