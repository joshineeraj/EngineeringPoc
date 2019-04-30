
var authToken = null;
var viewModel = {
    title: ko.observable(),
    description:ko.observable(),
    selected_priority: ko.observable(),
    selected_client: ko.observable(), 
    selected_production_area: ko.observable(), 
    target_date:ko.observable(),
    rows: ko.observableArray(),
    clients:ko.observableArray(),
    productionAreas:ko.observableArray(),
    count: ko.observable(),
    getAuthToken: function(callback){
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
        $.ajax({
            type: 'GET',
            url: api_path + "/feature_requests/",
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', 'Bearer '+authToken);
            },
            context: this,
            success: function(data) {
                this.rows(data.results);
                this.count(data.count);
            }.bind(this)
        });
    },
    createFeatureRequest: function(){
        
        $.ajax({
            type: 'POST',
            url: api_path + "/feature_requests/",
            data: {
                priority:this.selected_priority,
                client:this.selected_client,
                title:this.title,
                description:this.description,
                production_area: this.selected_production_area,
                target_date:this.target_date
            },
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', 'Bearer '+authToken);
            },    
            context: this,
            success: function(data) {
                this.rows.push(data);
                this.count(this.count()+1);
            }.bind(this)
        });
    }
};
ko.applyBindings(viewModel);

$(document).ready(function() {
    /* Populate list of feature requests in a table through API call */
    if(authToken==null){
        viewModel.getAuthToken();
    }
    
});