/* MagicMirror² Config Sample
 *
 * By Michael Teeuw https://michaelteeuw.nl
 * MIT Licensed.
 *
 * For more information on how you can configure this file
 * see https://docs.magicmirror.builders/configuration/introduction.html
 * and https://docs.magicmirror.builders/modules/configuration.html
 */
let config = {
	address: "localhost", 	// Address to listen on, can be:
							// - "localhost", "127.0.0.1", "::1" to listen on loopback interface
							// - another specific IPv4/6 to listen on a specific interface
							// - "0.0.0.0", "::" to listen on any interface
							// Default, when address config is left out or empty, is "localhost"
	port: 8080,
	basePath: "/", 	// The URL path where MagicMirror² is hosted. If you are using a Reverse proxy
					// you must set the sub path here. basePath must end with a /
	ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"], 	// Set [] to allow all IP addresses
															// or add a specific IPv4 of 192.168.1.5 :
															// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.1.5"],
															// or IPv4 range of 192.168.3.0 --> 192.168.3.15 use CIDR format :
															// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.3.0/28"],

	useHttps: false, 		// Support HTTPS or not, default "false" will use HTTP
	httpsPrivateKey: "", 	// HTTPS private key path, only require when useHttps is true
	httpsCertificate: "", 	// HTTPS Certificate path, only require when useHttps is true

	language: "en",
	locale: "en-US",
	logLevel: ["INFO", "LOG", "WARN", "ERROR"], // Add "DEBUG" for even more logging
	timeFormat: 24,
	units: "metric",
	// serverOnly:  true/false/"local" ,
	// local for armv6l processors, default
	//   starts serveronly and then starts chrome browser
	// false, default for all NON-armv6l devices
	// true, force serveronly mode, because you want to.. no UI on this device

	modules: [
		{
			module: "alert",
		},
		{
  module: 'MMM-SmartTouch', 
  position: 'bottom_center',    // This can be any of the regions.(bottom-center Recommended)
  config:{ 
    // None configuration options defined 
  }
},
		{
			module: "updatenotification",
			position: "top_bar"
		},
		{
			module: "clock",
			position: "top_left"
		},
		
		{
    module: 'MMM-MicrosoftToDo',
    position: 'top_left',	// This can be any of the regions. Best results in left or right regions.
    header: 'To Do', // This is optional
    config: {
      oauth2ClientSecret: 'lmZ8Q~y1GcPIQMZ1_iC2cojj~iLk03GmzGnQDc5E',
      oauth2RefreshToken: 'M.R3_BAY.-CYwbQb1EsixY8tkcWR6d9etZyDD*pMRnjTk1dm1mR56AenQK!La0hS1ZY*tEGG0piS!zooN99upOdn!mMOrcR20QFhz4wAN!wJlk8lpyNm0PVYCzg9x4c48MmrdERBhN9QM3DTtjNb9MeD5!nFUDWOXsIeyf2kke!1fyQS6qjAD*m3WVAh9UIIlkVhP7HFsmpA*l4c6!V7m3qvetJzp3jM3wAQU6hsXN0aVGI6QdwTfhAtiMeIK0dkzvJnIYQ4fxCiMDSw!CK1zouB*sS1ALRgUZuTSU4VDQtDFNrUprcsnkVuExd20CwXElfQ*qD58N1RZ*DlSgM!j0QdlPAP0l7w4By0Bm0FLTTvu88AP9ZdGv',
      oauth2ClientId: '0671a672-7a0a-48d5-be46-5d7e1375d78e',
      //listName: 'To Do', // optional parameter: if not specified displays tasks from default "Tasks" list, if specified will look for a task list with the specified name (exact spelling), don't specify if you want to make use of the 'includedLists' configuration property of the 'plannedTasks' configuration.
      // Optional parameter:  see Planned Tasks Configuration
      plannedTasks: {
        enable: false
      },
      showCheckbox: true, // optional parameter: default value is true and will show a checkbox before each todo list item
      showDueDate: false, // optional parameter: default value is false and will show the todo list items due date if it exists on the todo list item
      dateFormat: 'ddd MMM Do [ - ]', //optional parameter: uses moment date format and the default value is 'ddd MMM Do [ - ]'
      useRelativeDate: true, // optional parameter: default value is false and will display absolute due date, if set to false will show time in hours/days until item is due (midnight of due date)
      highlightTagColor: '#E3FF30', // optional parameter: highlight tags (#Tags) in the entry text. value can be a HTML color value
      hideIfEmpty: false, // optional parameter: default value is false and will show the module also when the todo list is empty
      maxWidth: 450, // optional parameter: max width in pixel, default value is 450
      itemLimit: 200, // optional parameter: limit on the number of items to show from the list, default value is 200
      orderBy: 'createdDate', // optional parameter: 'createdDate' - order results by creation date, 'dueDate' - order results by due date, default value is unordered, ordering by title is not supported anymore in API version 1
      completeOnClick: true, // optional parameter: default value is false, when set to true complete task when clicking on it
      refreshSeconds: 60, // optional parameter: every how many seconds should the list be updated from the remote service, default value is 60
      fade: true, //optional parameter: default value is false. True will fade the list towards the bottom from the point set in the fadePoint parameter
      fadePoint: 0.5, //optional parameter: decimal value between 0 and 1 sets the point where the fade effect will start,
      colorDueDate: true // optional parameter: default value is false.  True will display colors for overdue (red), upcoming (orange), and future (green) dates
    }
  },
		
		{
			module: "newsfeed",
			position: "bottom_bar",
			config: {
				feeds: [
					{
						title: "New York Times",
						url: "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
					}
				],
				showSourceTitle: true,
				showPublishDate: true,
				broadcastNewsFeeds: true,
				broadcastNewsUpdates: true
			}
		},
		{
			module: "weather",
			position: "top_right",
			header: "Weather Forecast",
			config: {
				weatherProvider: "openweathermap",
				type: "forecast",
				location: "New York",
				locationID: "5128581", //ID from http://bulk.openweathermap.org/sample/city.list.json.gz; unzip the gz file and find your city
				apiKey: "473f38bee4436b75da74c8fecfc957d8"
			}
		},
		{
    module: 'MMM-GoogleCalendar',
    header: "Upcoming Events",
    position: "top_center",
    config: {
		fetchInterval: 6000,
        calendars: [
            {
              symbol: "calendar-week",
              calendarID: "mjk289@cornell.edu"
            },
            // add another calendar HERE if needed
        ],
    }
},
	]
};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") {module.exports = config;}
