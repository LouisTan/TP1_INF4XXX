#!/usr/bin/env zsh

# Au préalable, je vous conseil de séparer vos séries en trois dossiers. Pour ce
# faire, allez dans le dossier qui contient tout le data et entrez les commandes
# suivantes:
#
# mkdir ../serie1 ../serie2 ../serie3
# cp $(ls | grep "testset_[0-9]\+_[0-9].txt") ../serie1
# cp $(ls | grep "testset_[0-9]\+_1[0-9].txt") ../serie2
# cp $(ls | grep "testset_[0-9]\+_2[0-9].txt") ../serie3
#
# Vous pouvez par après vous inspirer de ce script pour évaluer toutes les
# séries avec tous les algorithmes.

#ORIGINAL
# for algo in {"counting","quick","quickRandom","quickSeuil","quickRandomSeuil"}; do
#     # Pour chaque fichier de série.
#     for serie in {"serie1","serie2","serie3"}; do
#         # Pour chaque exemplaire dans une série.
#         for ex in $(ls $serie); do
#             # On receuille le temps d'exécution dans t.
#             t=$(timeout 180 ./tp.sh -a $algo -e ${serie}/${ex} -t)
#             # On évalue la taille de l'exemplaire.
#             n=$(cat ${serie}/${ex} | wc -l)
#             # Si jamais on mesure un temps, on l'insère dans le bon fichier.
#             if [ t != "" ]; then
#                 echo $n,$t >> ./${algo}_${serie}.csv
#             fi
#         done
#     done
# done

#RANDOM AlGO
# for algo in {"quickRandom","quickRandomSeuil"}; do
#     # Pour chaque fichier de série.
#     for x in {1..9}; do
#         for serie in {"serie1","serie2","serie3"}; do
#             # Pour chaque exemplaire dans une série.
#             for ex in $(ls $serie); do
#                 # On receuille le temps d'exécution dans t.
#                 t=$(timeout 180 ./tp.sh -a $algo -e ${serie}/${ex} -t)
#                 # On évalue la taille de l'exemplaire.
#                 n=$(cat ${serie}/${ex} | wc -l)
#                 # Si jamais on mesure un temps, on l'insère dans le bon fichier.
#                 if [ t != "" ]; then
#                     echo $n,$t >> ./${algo}_${serie}$x.csv
#                 fi
#             done
#         done
#     done
# done

#SEUIL
# Pour chaque fichier de série.
for serie in {"serie1","serie2","serie3"}; do
    # Pour chaque exemplaire dans une série.
    for ex in $(ls $serie); do
        for seuil in {1,5,10,15,20,25}; do
            # On receuille le temps d'exécution dans t.
            t=$(timeout 180 ./tp.sh -a quickSeuil -s ${seuil} -e ${serie}/${ex} -t)
            # Si jamais on mesure un temps, on l'insère dans le bon fichier.
            if [ t != "" ]; then
                echo $seuil,$t >> ./quickSeuil_${serie}.csv
            fi
        done
    done
done
