(ns game-of-life.core
    (:refer-clojure :exclude [==])
    (:use [clojure.core logic])
    )
(defn game [state action new-state]
      (== new-state state)
)


(defn -main [& args]
      (println (run 1 [q] (game 1 1 q)))
)
