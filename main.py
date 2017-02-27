str = """Alabama
Birmingham
Montgomery
Mobile
Huntsville
Tuscaloosa
Hoover
Alaska
Anchorage
Fairbanks
Juneau
Sitka
Ketchikan
Wasilla
Arizona
Phoenix
Tucson
Mesa
Chandler
Glendale
Scottsdale
Arkansas
Little Rock
Fort Smith
Fayetteville
Springdale
Jonesboro
North Little Rock
California
Los Angeles
San Diego
San Jose
San Francisco
Fresno
Sacramento
Colorado
Denver
Colorado Springs
Aurora
Fort Collins
Lakewood
Thornton
Connecticut
Bridgeport
New Haven
Hartford
Stamford
Waterbury
Norwalk
Delaware
Wilmington
Dover
Newark
Middletown
Smyrna
Milford
Florida
Jacksonville
Miami
Tampa
St Petersburg
Orlando
Hialeah
Georgia
Atlanta
Augusta
Columbus
Savannah
Athens
Sandy Springs
Hawaii
Honolulu
Pearl City
Hilo
Kailua
Waipahu
Kane'ohe
Idaho
Boise
Nampa
Meridian
Idaho Falls
Pocatello
Caldwell
Illinois
Chicago
Aurora
Rockford
Joliet
Naperville
Springfield
Indiana
Indianapolis
Fort Wayne
Evansville
South Bend
Hammond
Bloomington
Iowa
Des Moines
Cedar Rapids
Davenport
Sioux City
Waterloo
Iowa City
Kansas
Wichita
Overland Park
Kansas City
Topeka
Olathe
Lawrence
Kentucky
Louisville
Lexington-Fayette
Bowling Green
Owensboro
Covington
Hopkinsville
Louisiana
New Orleans
Baton Rouge
Shreveport
Lafayette
Lake Charles
Kenner
Maine
Portland
Lewiston
Bangor
South Portland
Auburn
Biddeford
Maryland
Baltimore
Frederick
Rockville
Gaithersburg
Bowie
Hagerstown
Massachusetts
Boston
Worcester
Springfield
Lowell
Cambridge
New Bedford
Michigan
Detroit
Grand Rapids
Warren
Sterling Heights
Lansing
Ann Arbor
Minnesota
Minneapolis
Saint Paul
Rochester
Duluth
Bloomington
Brooklyn Park
Mississippi
Jackson
Gulfport
Southaven
Hattiesburg
Biloxi
Meridian
Missouri
Kansas City
Saint Louis
Springfield
Independence
Columbia
Lee's Summit
Montana
Billings
Missoula
Great Falls
Bozeman
Butte-Silver Bow
Helena
Nebraska
Omaha
Lincoln
Bellevue
Grand Island
Kearney
Fremont
Nevada
Las Vegas
Henderson
Reno
North Las Vegas
Sparks
Carson City
New Hampshire
Manchester
Nashua
Concord
Dover
Rochester
Keene
New Jersey
Newark
Jersey City
Paterson
Elizabeth
Trenton
Clifton
New Mexico
Albuquerque
Las Cruces
Rio Rancho
Santa Fe
Roswell
Farmington
New York
New York
Buffalo
Rochester
Yonkers
Syracuse
Albany
North Carolina
Charlotte
Raleigh
Greensboro
Winston-Salem
Durham
Fayetteville
North Dakota
Fargo
Bismarck
Grand Forks
Minot
West Fargo
Mandan
Ohio
Columbus
Cleveland
Cincinnati
Toledo
Akron
Dayton
Oklahoma
Oklahoma City
Tulsa
Norman
Broken Arrow
Lawton
Edmond
Oregon
Portland
Eugene
Salem
Gresham
Hillsboro
Beaverton
Pennsylvania
Philadelphia
Pittsburgh
Allentown
Erie
Reading
Scranton
Rhode Island
Providence
Warwick
Cranston
Pawtucket
East Providence
Woonsocket
South Carolina
Columbia
Charleston
North Charleston
Mount Pleasant
Rock Hill
Greenville
South Dakota
Sioux Falls
Rapid City
Aberdeen
Brookings
Watertown
Mitchell
Tennessee
Memphis
Nashville
Knoxville
Chattanooga
Clarksville
Murfreesboro
Texas
Houston
San Antonio
Dallas
Austin
Fort Worth
El Paso
Utah
Salt Lake City
West Valley City
Provo
West Jordan
Orem
Sandy
Vermont
Burlington
South Burlington
Rutland
Essex Junction
Barre
Montpelier
Virginia
Virginia Beach
Norfolk
Chesapeake
Richmond
Newport News
Alexandria
Washington
Seattle
Spokane
Tacoma
Vancouver
Bellevue
Kent
West Virginia
Charleston
Huntington
Parkersburg
Morgantown
Wheeling
Weirton
Wisconsin
Milwaukee
Madison
Green Bay
Kenosha
Racine
Appleton
Wyoming
Cheyenne
Casper
Laramie
Gillette
Rock Springs
Sheridan"""


count = 0
for i in str.splitlines():
    count += 1
    print("[\"" + i + "\"] ",end= "")
    if count == 7:
        print('\n')
        count = 0
