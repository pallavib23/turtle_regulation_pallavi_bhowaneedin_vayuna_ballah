# turtle_regulation_pallavi_bhowaneedin_vayuna_ballah

 

TP-1 Note : Turtle Regulation Package-INFO-2
Written by:
Pallavi Bhowaneedin
Vayuna Ballah

La simulation de tortue est une simulation qui est faite afin de calculer l'angle de déplacement.
TURTLE REGUALATION REGULATION
Ce package permet de reguler le movement d'une autre tortue dans turtlesim en utilisant la regulation en cap et en distance.

 # Turtle Waypoint Navigator

The Turtle Waypoint Navigator is a ROS (Robot Operating System) package that allows a turtle to navigate towards a predefined waypoint in a turtlesim environment. It uses proportional control to adjust the turtle's angular velocity based on the error between the current position and the waypoint.

## Prerequisites

- ROS (Robot Operating System) installed
- turtlesim package installed

## Installation

1. Clone the repository into your catkin workspace:

```bash
cd <your_catkin_workspace>/src
git clone <repository_url>
```


Creation du launch File
Creez un fichier 'launch_file.launch' dans votre package
Ouvrez le fichier 'launch_file.launch' avec un editeur de texte.
Ajoutez le contenu suivant pour lancer tous les noeuds necessaires.
Lancement du noeud set_way_point.py
```sh
<node name="set_way_point_node" pkg ="my_package" 
type="set_way_point.py" output="screen"/>
````

 

#lancement du noeud regulation_en_cap.py
```sh
<node name="regulation_en_cap_node" pkg="my_package" 
type="regulation_en_cap.py" output="screen"/>
```
 


#lancement du noeud regulation_en_distance.py
```sh
<node name="regulation_en_distance_node" pkg="my_package" 
type="regulation_en_distance.py" output="screen"/>
```
 #note
 please run this code in the bash to run partie 2
 ```sh
 rosrun <package_name> <node_name> _distance_tolerance:=0.05
```
