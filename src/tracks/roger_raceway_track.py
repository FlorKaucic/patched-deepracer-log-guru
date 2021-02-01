from src.tracks.track import Track
import src.configuration.personal_track_annotations as config


class RogerRacewayTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Roger Raceway"
        self._ui_description = "The Roger Raceway is named in honor of the 2019 Championship Cup bronze medalist Roger Chu."
        self._ui_length_in_m = 60  # metres
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "July_2020"
        self._track_sector_dividers = [0, 10, 20]  # Sectors TODO
        self._annotations = config.roger_raceway_annotations
        self._track_width = 0.914

        self._track_waypoints = [
                         [-0.730726957321167, -0.8597202152013779],
                         [-1.1528210043907166, -0.860040083527565],
                         [-1.5706024765968323, -0.8600375205278397],
                         [-1.9126494526863098, -0.8600291311740875],
                         [-2.245930552482605, -0.8600251525640488],
                         [-2.5782164335250854, -0.8600473701953888],
                         [-2.9105329513549805, -0.8600390702486038],
                         [-3.242935538291931, -0.8599974513053894],
                         [-3.575163960456848, -0.860090434551239],
                         [-3.907320499420166, -0.8600515574216843],
                         [-4.239967584609985, -0.8587584048509598],
                         [-4.572450399398804, -0.8512996733188629],
                         [-4.903303623199463, -0.8300447165966034],
                         [-5.232973575592041, -0.7904577404260635],
                         [-5.560291528701782, -0.7261287271976471],
                         [-5.8724753856658936, -0.6151338890194893],
                         [-6.1529505252838135, -0.4394827075302601],
                         [-6.383931398391724, -0.20243874471634626],
                         [-6.5537495613098145, 0.08377861604094505],
                         [-6.660109519958496, 0.3987950533628464],
                         [-6.70038628578186, 0.7266036868095398],
                         [-6.674363851547241, 1.0564639270305634],
                         [-6.612706184387207, 1.3845030069351196],
                         [-6.553715467453003, 1.7107020020484924],
                         [-6.491829872131348, 2.036399483680725],
                         [-6.4147725105285645, 2.361707925796509],
                         [-6.329217433929443, 2.682299017906189],
                         [-6.239607095718384, 2.9990044832229614],
                         [-6.1402904987335205, 3.3206080198287964],
                         [-5.998764991760254, 3.6210219860076904],
                         [-5.7643492221832275, 3.8439905643463135],
                         [-5.456943988800049, 3.977376103401184],
                         [-5.130693435668945, 4.0386223793029785],
                         [-4.8003339767456055, 4.062419891357422],
                         [-4.467580556869507, 4.079571008682251],
                         [-4.135386943817139, 4.091871976852417],
                         [-3.804479479789734, 4.097510933876038],
                         [-3.471471071243286, 4.098227024078369],
                         [-3.137386441230774, 4.103309392929077],
                         [-2.807526469230652, 4.127366423606873],
                         [-2.4782004356384277, 4.160015940666199],
                         [-2.1433154344558716, 4.184657096862793],
                         [-1.8170075416564941, 4.242341637611389],
                         [-1.5169219970703125, 4.3768675327301025],
                         [-1.2475636303424835, 4.570746421813965],
                         [-1.0046806633472443, 4.797316551208496],
                         [-0.7728899121284485, 5.036941051483154],
                         [-0.5468903481960297, 5.281199932098389],
                         [-0.3330457368865609, 5.533026456832886],
                         [-0.12278660386800766, 5.789509534835815],
                         [0.10331225395202637, 6.0384840965271],
                         [0.3661130517721176, 6.236345529556274],
                         [0.6766382157802582, 6.3449156284332275],
                         [1.008580356836319, 6.391093969345093],
                         [1.3391125202178955, 6.411160469055176],
                         [1.6699550151824951, 6.430063962936401],
                         [2.001839518547058, 6.461933135986328],
                         [2.3308005332946777, 6.509123086929321],
                         [2.656496524810791, 6.570728540420532],
                         [2.980981945991516, 6.644223928451538],
                         [3.3028165102005005, 6.728923082351685],
                         [3.6211220026016235, 6.821293592453003],
                         [3.943434476852417, 6.903234481811523],
                         [4.273377418518066, 6.947884559631348],
                         [4.6010565757751465, 6.9174888134002686],
                         [4.9129884243011475, 6.801005601882935],
                         [5.194824457168579, 6.625088453292847],
                         [5.455374002456665, 6.420198917388916],
                         [5.721442699432373, 6.219642639160156],
                         [6.015071392059326, 6.071527004241943],
                         [6.344783306121826, 6.022107362747192],
                         [6.671466112136841, 6.079229116439819],
                         [6.964423418045044, 6.225775480270386],
                         [7.245023488998413, 6.40904688835144],
                         [7.5362229347229, 6.57170557975769],
                         [7.850999593734741, 6.660508394241333],
                         [8.184367656707764, 6.677988767623901],
                         [8.518070220947266, 6.670707941055298],
                         [8.84804105758667, 6.650393009185791],
                         [9.177337169647217, 6.611875534057617],
                         [9.506917476654053, 6.558852672576904],
                         [9.830041408538818, 6.482084512710571],
                         [10.121128559112549, 6.33127760887146],
                         [10.34803056716919, 6.085774660110474],
                         [10.474605083465576, 5.781528949737549],
                         [10.492754936218262, 5.45290112495422],
                         [10.420539855957031, 5.1277689933776855],
                         [10.271928787231444, 4.830325126647947],
                         [10.060211658477785, 4.577461004257205],
                         [9.810254573822021, 4.358123064041138],
                         [9.545685768127441, 4.155564069747925],
                         [9.275564193725586, 3.962740898132324],
                         [9.005532264709473, 3.7714529037475586],
                         [8.740286350250244, 3.568686008453369],
                         [8.493128776550293, 3.3441214561462402],
                         [8.285827159881592, 3.0903834104537964],
                         [8.136801481246948, 2.797331929206848],
                         [8.065941572189331, 2.462602972984314],
                         [8.114450931549072, 2.138152539730072],
                         [8.308693885803223, 1.88577800989151],
                         [8.603835582733154, 1.7373449802398682],
                         [8.940667152404785, 1.707647979259491],
                         [9.260721206665039, 1.7904695272445679],
                         [9.537721633911133, 1.962689459323883],
                         [9.78199052810669, 2.1851009726524353],
                         [10.02088975906372, 2.4181125164031982],
                         [10.287700176239014, 2.621880054473877],
                         [10.5903000831604, 2.753293037414551],
                         [10.917824745178223, 2.7743325233459473],
                         [11.22859001159668, 2.669292449951172],
                         [11.480810165405273, 2.4483020305633545],
                         [11.646965026855469, 2.162719964981079],
                         [11.734300136566162, 1.8479414582252502],
                         [11.7861647605896, 1.5149974822998047],
                         [11.804519653320312, 1.179559051990509],
                         [11.764494895935059, 0.8580093085765839],
                         [11.670529842376709, 0.5419150441884995],
                         [11.531845092773438, 0.22745347768068314],
                         [11.328094959259033, -0.03197740018367767],
                         [11.050574779510498, -0.19457539916038513],
                         [10.730854988098145, -0.27350034564733505],
                         [10.39674997329712, -0.30044783651828766],
                         [10.063669681549072, -0.31968510895967484],
                         [9.734337329864502, -0.34574246034026146],
                         [9.403090953826904, -0.37083835899829865],
                         [9.070809841156006, -0.397166196256876],
                         [8.740366458892822, -0.42938085552304983],
                         [8.410090923309326, -0.4622483612038195],
                         [8.078509330749512, -0.4911332204937935],
                         [7.747377872467041, -0.5188368000090122],
                         [7.416916608810425, -0.5465065203607082],
                         [7.084786415100098, -0.5715410187840462],
                         [6.752209901809692, -0.5918854251503944],
                         [6.422557353973389, -0.6051406115293503],
                         [6.091045618057248, -0.6002605184912678],
                         [5.757177114486694, -0.5556382834911346],
                         [5.45870304107666, -0.42122114449739456],
                         [5.245318174362183, -0.16989151015877724],
                         [5.1684393882751465, 0.14602746069431305],
                         [5.225686550140381, 0.47623975574970245],
                         [5.335612535476685, 0.7936426401138306],
                         [5.458479881286621, 1.0955007076263428],
                         [5.5971410274505615, 1.3976625204086304],
                         [5.7445878982543945, 1.700013518333435],
                         [5.885759592056274, 1.9980275630950928],
                         [5.996119022369385, 2.310100555419922],
                         [6.039302110671997, 2.6435534954071045],
                         [5.954769134521484, 2.954745054244995],
                         [5.728879928588867, 3.1988445520401],
                         [5.430205345153809, 3.345335602760315],
                         [5.105846166610718, 3.4045034646987915],
                         [4.773513555526733, 3.422452449798584],
                         [4.441018581390381, 3.4163814783096313],
                         [4.11040997505188, 3.38789701461792],
                         [3.7801564931869507, 3.3509554862976074],
                         [3.4488860368728638, 3.317004084587097],
                         [3.1193634271621704, 3.276822090148926],
                         [2.792374014854431, 3.223841428756714],
                         [2.4645224809646606, 3.1617515087127686],
                         [2.150389075279236, 3.0593185424804688],
                         [1.9094035029411316, 2.884132504463196],
                         [1.7484610080718994, 2.571979522705078],
                         [1.7763584852218628, 2.24360454082489],
                         [1.936593472957611, 1.9427504539489746],
                         [2.131580948829651, 1.6764144897460938],
                         [2.320208966732025, 1.4075234532356262],
                         [2.4696850776672363, 1.1073395013809204],
                         [2.544708490371704, 0.7850798070430756],
                         [2.5369009971618652, 0.4545292556285858],
                         [2.467809557914734, 0.12959140166640282],
                         [2.3436149954795833, -0.17816414684057275],
                         [2.1591529846191406, -0.4559143893420696],
                         [1.9117285013198853, -0.6719367355108261],
                         [1.6069040298461914, -0.7987806797027588],
                         [1.2763720154762268, -0.8526110649108887],
                         [0.9454828500747681, -0.8617896884679794],
                         [0.6139589548110962, -0.8588589131832123],
                         [0.28090040385723114, -0.8599819988012314],
                         [-0.0515983197838068, -0.8606397807598114],
                         [-0.38474760949611664, -0.8598184734582901],
                         [-0.730726957321167, -0.8597202152013779]
        ]
