 import webhoseio

    webhoseio.config(token="50e8f8f7-33f3-4cfe-8b39-d5ae04c44b6b")
    query_params = {
	"q": "(\"West Texas Detention Facility\" OR \"Southwest Key Casa Padre\" OR \"West Texas Detention Facility\" OR \"Southwest Key Casa Padre\" OR \"Southwest Key San Benito/Casa Antigua\" OR \"Southwest Key Combes\" OR \"Southwest Key El Cajon\" OR \"Southwest Key Estrella del Norte\" OR \"Southwest Key Youngtown - Hacienda del Sol\" OR \"Southwest Key Glendale\" OR \"Southwest Key Conroe\" OR \"Joe Corley Detention Facility \" OR \"Southwest Key Casa Quetzal\" OR \"Southwest Key Casa Blanca\" OR \"Southwest Key Casa Montezuma\" OR \"Southwest Key Casa El Presidente\" OR \"Southwest Key Casa Grande\" OR \"Southwest Key Casa Franklin\" OR \"Southwest Key Nueva Esperanza\" OR \"Southwest Key Casa Houston Reliant\" OR \"Southwest Key Shelter Care\" OR \"Southwest Key Casita del Valle\" OR \"Southwest Key Pleasant Hill\" OR \"Southwest Key Las Palmas\" OR \"Southwest Key Lemon Grove\" OR \"Southwest Key La Esperanza Home for Boys\" OR \"Southwest Key Campbell\" OR \"Shiloh Treatment Center\" OR \"Shenendoah Valley Juvenile Center\" OR \"La Salle County Regional Detention Center\" OR \"Alice Peterson Residence \" OR \"Dorothy Mitchell Residence \" OR \"Msgr. Bryan Walsh's Children's Village \" OR \"Board of Childcare\" OR \"Brazoria County Youth Homes\" OR \"Galveston Multicultural Institute\" OR \"The Pelican Island Center\" OR \"Bethany Children's Home\" OR \"Yolo County Juvenile Detention Center\" OR \"Children's Home of Kingston\" OR \"Leake and Watts Passages of Hope\" OR \"Griffin Home Residential Programs - Maceachern House\" OR \"His House Children's Home\" OR \"Homestead Temporary Shelter for Unaccompanied Children\" OR \"Holy Family Institute\" OR \"Inwood House/The Children's Village\" OR \"McAllen Station\" OR \"Lincoln Hall\" OR \"Bokenkamp Children's Shelter\" OR \"Morrison Paso Staff Secure\" OR \"Morrison Knott Street\" OR \"Nuevo Amanecer Latino Children's Services\" OR \"Neighbor to Family\" ) site_type:news thread.country:US language:english",
	"ts": "1527911096744",
	"sort": "crawled"
    }
    output = webhoseio.query("filterWebContent", query_params)
    print output['posts'][0]['text'] # Print the text of the first post
    print output['posts'][0]['published'] # Print the text of the first post publication date

    
# Get the next batch of posts

    output = webhoseio.get_next()

    
# Print the site of the first post

    print output['posts'][0]['thread']['site']