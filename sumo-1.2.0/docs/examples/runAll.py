import subprocess,sys
for p in [
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/dfrouter", r"--write-license", r"--include-unused-routes", r"--measure-files", r"input_tri_flows.txt", r"--keep-longer-routes", r"--net-file=input_tri.net.xml", r"--detector-files=input_tri.det.xml", r"--routes-output", r"routes.rou.xml", r"--emitters-output", r"emitters.add.xml", r"-e", r"60"], cwd=r"/home/delphi/gcc/sumo/docs/examples/dfrouter"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/duarouter", r"--no-step-log", r"--write-license", r"--net-file=input_net.net.xml", r"--route-files=input_flows.flows.xml", r"-o", r"routes.rou.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/duarouter/flows2routes"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/duarouter", r"--no-step-log", r"--write-license", r"--net-file=input_net.net.xml", r"--route-files=input_flows.flows.xml", r"-o", r"routes.rou.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/duarouter/flows2routes_100s_interval"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/duarouter", r"--no-step-log", r"--write-license", r"--net-file=input_net.net.xml", r"--route-files=input_flows.flows.xml", r"-o", r"routes.rou.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/duarouter/flows2routes_100s_interval_ext"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/duarouter", r"--no-step-log", r"--write-license", r"--net-file=input_net.net.xml", r"--route-files=input_flows.flows.xml", r"-o", r"routes.rou.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/duarouter/flows2routes_200s_interval"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/duarouter", r"--no-step-log", r"--write-license", r"--net-file=input_net.net.xml", r"--route-files=input_trips.trips.xml", r"-o", r"routes.rou.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/duarouter/trips2routes"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/jtrrouter", r"--no-step-log", r"--write-license", r"--output-file=routes.rou.xml", r"--net-file=input_net.net.xml", r"--route-files=input_flows.flows.xml", r"--sinks=end", r"--turns=input_turns.turns.xml", r"--ignore-errors"], cwd=r"/home/delphi/gcc/sumo/docs/examples/jtrrouter/turns"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/jtrrouter", r"--no-step-log", r"--write-license", r"--net-file=input_net.net.xml", r"--route-files=input_flows.flows.xml", r"--output-file=routes.rou.xml", r"--turn-defaults=0,100,0,0", r"--sinks=end", r"--ignore-errors"], cwd=r"/home/delphi/gcc/sumo/docs/examples/jtrrouter/straight_only_sinks"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/netconvert", r"--write-license", r"--edge-files=input_edges.edg.xml", r"--connection-files", r"input_connections.con.xml", r"--node-files=input_nodes.nod.xml", r"--output=net.net.xml", r"--speed-in-kmh"], cwd=r"/home/delphi/gcc/sumo/docs/examples/netconvert/connections/cross3l_edge2edge_conns"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/netconvert", r"--write-license", r"--edge-files=input_edges.edg.xml", r"--connection-files=input_connections.con.xml", r"--node-files=input_nodes.nod.xml", r"--output=net.net.xml", r"--speed-in-kmh"], cwd=r"/home/delphi/gcc/sumo/docs/examples/netconvert/connections/cross3l_lane2lane_conns"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/netconvert", r"--write-license", r"--edge-files=input_edges.edg.xml", r"--node-files=input_nodes.nod.xml", r"--output=net.net.xml", r"--speed-in-kmh", r"--no-turnarounds"], cwd=r"/home/delphi/gcc/sumo/docs/examples/netconvert/connections/cross3l_no_turnarounds"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/netconvert", r"--write-license", r"--edge-files=input_edges.edg.xml", r"--connection-files", r"input_connections.con.xml", r"--node-files=input_nodes.nod.xml", r"--output=net.net.xml", r"--speed-in-kmh"], cwd=r"/home/delphi/gcc/sumo/docs/examples/netconvert/connections/cross3l_prohibitions"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/netconvert", r"--write-license", r"--edge-files=input_edges.edg.xml", r"--node-files=input_nodes.nod.xml", r"--output=net.net.xml", r"--speed-in-kmh"], cwd=r"/home/delphi/gcc/sumo/docs/examples/netconvert/connections/cross3l_unconstrained"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/netconvert", r"--write-license", r"--edge-files=input_edges.edg.xml", r"--node-files=input_nodes.nod.xml", r"--output=net.net.xml", r"--plain-output=plain", r"--plain.extend-edge-shape"], cwd=r"/home/delphi/gcc/sumo/docs/examples/netconvert/hokkaido"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/netconvert", r"--write-license", r"--edge-files=input_edges.edg.xml", r"--node-files=input_nodes.nod.xml", r"--connection-files=input_connections.con.xml", r"--output=net.net.xml", r"--no-turnarounds"], cwd=r"/home/delphi/gcc/sumo/docs/examples/netconvert/dlr-testtrack"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/netconvert", r"--write-license", r"--edge-files=input_edges.edg.xml", r"--node-files=input_nodes.nod.xml", r"--output=net.net.xml", r"--speed-in-kmh"], cwd=r"/home/delphi/gcc/sumo/docs/examples/netconvert/speed_in_kmh/cross_notypes_kmh"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/netconvert", r"--write-license", r"--edge-files=input_edges.edg.xml", r"--node-files=input_nodes.nod.xml", r"--type-files=input_types.typ.xml", r"--output=net.net.xml", r"--speed-in-kmh"], cwd=r"/home/delphi/gcc/sumo/docs/examples/netconvert/speed_in_kmh/cross_usingtypes_kmh"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/netconvert", r"--write-license", r"--edge-files=input_edges.edg.xml", r"--node-files=input_nodes.nod.xml", r"--output=net.net.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/netconvert/types/cross_notypes"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/netconvert", r"--write-license", r"--edge-files=input_edges.edg.xml", r"--node-files=input_nodes.nod.xml", r"--type-files=input_types.typ.xml", r"--output=net.net.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/netconvert/types/cross_usingtypes"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/netconvert", r"--write-license", r"--no-internal-links", r"--osm-files", r"osm.xml", r"-v", r"--proj.utm", r"--output.street-names", r"--plain-output-prefix", r"plain", r"--proj.plain-geo", r"--output", r"net.net.xml", r"--tls.red.time", r"10"], cwd=r"/home/delphi/gcc/sumo/docs/examples/netconvert/OSM/adlershof_dlr"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"--routes=input_routes.rou.xml", r"-b", r"0", r"-e", r"10000"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/hokkaido"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"-b", r"0", r"-e", r"1000", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"--routes=input_routes.rou.xml", r"-a", r"input_additional.add.xml,input_additional2.add.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/variable_speed_signs"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"--routes=input_routes.rou.xml", r"--vehroute-output", r"vehroutes.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/vehicle_stops"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"-a=input_additional.add.xml", r"--vehroutes=vehroutes.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/busses"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"-n", r"net.net.xml", r"--route-files=input_routes.rou.xml", r"--additional-files=input_additional.add.xml", r"--fcd-output", r"fcd.xml", r"--fcd-output.signals"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/angled_roadside_parking"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"--routes=input_routes.rou.xml", r"--time-to-teleport", r"-1"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/visualization/parade"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--emission-output=emissions.xml", r"--net-file=net.net.xml", r"-r", r"input_routes.rou.xml", r"-b", r"0", r"-e", r"120"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/output/cross3ltl_emission"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--fcd-output=fcd.xml", r"--net-file=net.net.xml", r"-r", r"input_routes.rou.xml", r"-b", r"0", r"-e", r"120"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/output/cross3ltl_fcd"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--full-output=full.xml", r"--net-file=net.net.xml", r"-r", r"input_routes.rou.xml", r"-b", r"0", r"-e", r"120"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/output/cross3ltl_full"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"-r", r"input_routes.rou.xml", r"-a", r"input_additional.add.xml", r"-b", r"0", r"-e", r"1000"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/output/cross3ltl_inductloops"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"-r", r"input_routes.rou.xml", r"-a", r"input_additional.add.xml", r"-b", r"0", r"-e", r"1000"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/output/cross3ltl_meandata_constrained"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"-r", r"input_routes.rou.xml", r"-a", r"input_additional.add.xml", r"-b", r"0", r"-e", r"1000"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/output/cross3ltl_meandata_edges"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"-r", r"input_routes.rou.xml", r"-a", r"input_additional.add.xml", r"-b", r"0", r"-e", r"1000"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/output/cross3ltl_meandata_lanes"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--queue-output=queue.xml", r"--net-file=net.net.xml", r"-r", r"input_routes.rou.xml", r"-b", r"0", r"-e", r"200"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/output/cross3ltl_queue"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--netstate-dump=rawdump.xml", r"--net-file=net.net.xml", r"-r", r"input_routes.rou.xml", r"-b", r"90", r"-e", r"120"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/output/cross3ltl_rawdump"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"-r", r"input_routes.rou.xml", r"--summary=summary.xml", r"-b", r"0", r"-e", r"1000"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/output/cross3ltl_summary"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--tripinfo-output=tripinfos.xml", r"--net-file=net.net.xml", r"-r", r"input_routes.rou.xml", r"-b", r"0", r"-e", r"1000"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/output/cross3ltl_tripinfo"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--vehroute-output=vehroutes.xml", r"--net-file=net.net.xml", r"-r", r"input_routes.rou.xml", r"-b", r"0", r"-e", r"1000"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/output/cross3ltl_vehroutes"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"-r", r"input_routes.rou.xml", r"-a", r"input_additional.add.xml", r"-b", r"0", r"-e", r"220"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/output/cross3ltl_vtypeprobe"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--time-to-teleport", r"-1", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"--routes=input_routes.rou.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/simple_nets/cross/cross1ltl"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--time-to-teleport", r"-1", r"-v", r"--no-step-log", r"--net-file=net.net.xml", r"--routes=input_routes.rou.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/simple_nets/cross/cross1l"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--time-to-teleport", r"-1", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"--routes=input_routes.rou.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/simple_nets/cross/cross3ltl"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--time-to-teleport", r"-1", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"--routes=input_routes.rou.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/simple_nets/cross/cross3l"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--time-to-teleport", r"-1", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"--routes=input_routes.rou.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/simple_nets/box/box1l"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--time-to-teleport", r"-1", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"--routes=input_routes.rou.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/simple_nets/box/box2l"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--time-to-teleport", r"-1", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"--routes=input_routes.rou.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/simple_nets/box/box3l"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--time-to-teleport", r"-1", r"--no-step-log", r"--no-duration-log", r"--net-file=net.net.xml", r"--routes=input_routes.rou.xml"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/simple_nets/box/box4l"),
    subprocess.Popen([r"/home/delphi/gcc/sumo/bin/sumo", r"--write-license", r"--default.speeddev", r"0", r"--no-step-log", r"--net-file=net.net.xml", r"--routes=input_routes.rou.xml", r"--lateral-resolution", r"0.64", r"--tripinfo-output", r"tripinfos.xml", r"--duration-log.statistics"], cwd=r"/home/delphi/gcc/sumo/docs/examples/sumo/sublane_model"),
    subprocess.Popen([r"python", r"/home/delphi/gcc/sumo/tools/assign/duaIterate.py", r"-n", r"input_net.net.xml", r"-t", r"input_trips.trips.xml", r"-l", r"5"], cwd=r"/home/delphi/gcc/sumo/docs/examples/tools/dua-iterate"),
    subprocess.Popen([r"python", r"/home/delphi/gcc/sumo/tools/detector/flowrouter.py", r"-n", r"input_net.net.xml", r"-d", r"input_detectors.det.xml", r"-f", r"input_flows.txt", r"--verbose"], cwd=r"/home/delphi/gcc/sumo/docs/examples/tools/flowrouter"),
    subprocess.Popen([r"python", r"/home/delphi/gcc/sumo/tools/traceExporter.py", r"-i", r"fcd.xml", r"-n", r"net.net.xml", r"--ns2mobility-output", r"mobilityfile.tcl"], cwd=r"/home/delphi/gcc/sumo/docs/examples/tools/traceExporter"),
    subprocess.Popen([r"python", r"./runner.py"], cwd=r"/home/delphi/gcc/sumo/docs/tutorial/quickstart"),
    subprocess.Popen([r"python", r"./runner.py"], cwd=r"/home/delphi/gcc/sumo/docs/tutorial/hello"),
    subprocess.Popen([r"python", r"./runner.py", r"--nogui"], cwd=r"/home/delphi/gcc/sumo/docs/tutorial/traci_tls"),
    subprocess.Popen([r"python", r"./runner.py"], cwd=r"/home/delphi/gcc/sumo/docs/tutorial/manhattan"),
]:
    if p.wait() != 0:
        sys.exit(1)