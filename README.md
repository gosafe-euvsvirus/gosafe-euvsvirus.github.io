# gosafe.github.io
EUvsVirus project

## How we built it
### Dataset
We started downloading up to 13000 POI locations from the [Barcelona Open Data Portal](https://opendata-ajuntament.barcelona.cat/data/en/dataset), including bus, metro, train, tram stations, hospitals, clinics, supermarkets, grocery shops, libraries, etc. We want kids as far away as possible from crowded places, and accordingly we have assigned risk scores to each category. Using `python` and `QGIS`, we have created risk matrices for each category in `netCDF` format, each score element covering an area of 10x10 meters. Adding up all the matrices multiplied by its score (category risk score) we finally got the CoVid-19 risk map for barcelona. We scaled the values and applied a color ramp to create an image using `OpenCV`. Scripts used can be found in the [GoSave github](https://github.com/gosafe-euvsvirus/gosafe-euvsvirus.github.io). To share the risk map we created a [GoSave map](https://gosafe-euvsvirus.github.io/) through a simple `Leaflet` application. 

### Back-end ops
All the `netCDF` files are stored in the back-end so when the client request a position score through the API, it can answer as fast as possible. These score matrices are also looked up when the player stats a new game. In this case, an algo choose a random route destination, located between 600 and 800 meters from the origin and checking that the proposed location has an associated risk above a threshold. The back-end also stores each new possition sent by the client during a walk so at the end it can send total score and store past walks in a `MongoDB` database.

### API
In order to do that a [GoSave API](https://app.swaggerhub.com/apis/jaumebrossa/GoSafeAPI/1.0.0#/) has been created using `Swagger`. It has the following endpoints and operations:

**game** *(Everything used while playing)*
* **GET** **/game/destination/{start}** --> Get destination for the current game
* **GET** **/game/score/{position}** --> Get actual score for current position
* **POST** **/game/score/{position}** --> Post current position
* **GET** **/game/totalscore/** --> Get total score for current game


**user** *(Operations about user)*
* **POST** **/user** --> Logs out current logged in user session
* **GET** **/user/login** --> Logs user into the system
* **GET** **/user/logout** --> Logs out current logged session
* **GET** **/user/pastroutes/** --> Get historic of past routes
* **GET** **/user/pastscores/** --> Get historic of past scores
* **GET** **/user/{username}** --> Get user by username
* **PUT** **/user/{username}** --> Update user
* **DELETE** **/user/{username}** --> Delete user
* **GET** **/game/destination/{start}** --> Get destination for the current game

**decision** *(Reports and utilities used for social public safety administrations)*
* **GET** **/decision/allroutes/{date}** --> Returns all routes performed in the given day
* **GET** **/decision/dangerzones** --> Returns all danger zones with their scores
* **POST** **/decision/dangerzones** --> Post new danger zones to be included in the app


