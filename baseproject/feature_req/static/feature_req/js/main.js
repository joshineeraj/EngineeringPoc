
/*Global variable to store authToken to be used in all requests */
var authToken = null;


/* Adding viewModel */
currentDate = (new Date()).toISOString().split('T')[0];
var viewModel = {
    title: ko.observable("Title").extend({required: true}),
    description:ko.observable(),
    selected_priority: ko.observable(1).extend({ min: 1 }),
    selected_client: ko.observable(), 
    selected_production_area: ko.observable(), 
    target_date:ko.observable(currentDate).extend({required: true}).extend({min: currentDate }),
    rows: ko.observableArray(),
    clients:ko.observableArray(),
    productionAreas:ko.observableArray(),
    count: ko.observable(),
   
    getAuthToken: function(){
        /* Authenticates user, gets the authToken and then Store it in global variable */
        $.post(api_path + "/get-auth-token/", 
            {"username":"api_user", 
            "password":"api_password"
            },
            function(data){
                authToken = data.token;
                this.getClients(); 
                this.getProductionAreas();
                this.getFeatureRequests();
            }.bind(this)
        );
    },
    getClients: function(){
        /* Populate the Client list in Clients Dropdown */
        $.ajax({
            type: 'GET',
            url: api_path + "/clients/",
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', 'Bearer '+authToken);
            },
            context: this,
            success: function(data) {
                this.clients(data.results);
            }.bind(this)
        });
    },
    getProductionAreas: function(){
        /*Populate the Production area in the production area dropdown */
        $.ajax({
            type: 'GET',
            url: api_path + "/production_areas/",
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', 'Bearer '+authToken);
            },
            context: this,
            success: function(data) {
                this.productionAreas(data.results);
            }.bind(this)
        });
    },
    getFeatureRequests: function() {
        /* Populate list of feature requests in a table through API call */
        /*Get all feature requests */
        $.ajax({
            type: 'GET',
            url: api_path + "/feature_requests/",
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', 'Bearer '+authToken);
            },
            context: this,
            success: function(data) {
                /* Add the fetched data to 'rows' observable array*/
                this.rows(data.results);
                /*Fetch and update the count of the records */
                this.count(data.count);
            }.bind(this)
        });
    },
    createFeatureRequest: function(){
        /*Create a Feature request. */
        post_data = {
            priority:this.selected_priority,
            client:this.selected_client,
            title:this.title,
            description:this.description,
            production_area: this.selected_production_area,
            target_date:this.target_date
        }
        $.ajax({
            type: 'POST',
            url: api_path + "/feature_requests/",
            data: post_data,
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', 'Bearer '+authToken);
            },    
            context: this,
            success: function(data) {
                this.getFeatureRequests();
            }.bind(this), 
            error: function(errors){
                debugger;
            }

        });
    }
};
ko.applyBindings(viewModel);

$(document).ready(function() {
    if(authToken==null){
        viewModel.getAuthToken();
    }

});


