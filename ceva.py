# # while self.finalSet == False:
# #     if self.first_server_to_serve == True:
# #         newGame = Game(0, 0, False)
# #         self.listaGames.append(newGame)
# #         if newGame.winner == True:
# #             self.gamesCastigatePlayer1 += 1
# #         else:
# #             self.gamesCastigatePlayer2 += 1
# #     else:
# #         newGame = Game(0, 0, False)
# #         self.listaGames.append(newGame)
# #         if newGame.winner == True:
# #             self.gamesCastigatePlayer2 += 1
# #         else:
# #             self.gamesCastigatePlayer1 += 1
# #     # print("self.gamesCastigatePlayer1", self.gamesCastigatePlayer1)
# #     # print("self.gamesCastigatePlayer2", self.gamesCastigatePlayer2)
# #
# #     if self.gamesCastigatePlayer1 == self.targetGames:
# #         if self.gamesCastigatePlayer2 == self.targetGames:
# #             varTiebreakGame = self.playTiebreak()
# #             if self.first_server_to_serve == True:
# #                 if varTiebreakGame == True:
# #                     self.gamesCastigatePlayer1 += 1
# #                     self.finalSet = True
# #                     return True
# #                 else:
# #                     self.gamesCastigatePlayer2 += 1
# #                     self.finalSet = True
# #                     return False
# #             else:
# #                 if varTiebreakGame == True:
# #                     self.gamesCastigatePlayer2 += 1
# #                     self.finalSet = True
# #                     return False
# #                 else:
# #                     self.gamesCastigatePlayer1 += 1
# #                     self.finalSet = True
# #                     return True
# #
# #         if self.gamesCastigatePlayer1 - self.gamesCastigatePlayer2 >= 2:
# #             self.finalSet = True
# #             return True
# #     elif self.gamesCastigatePlayer1 == self.targetGames + 1:
# #         if self.gamesCastigatePlayer1 - self.gamesCastigatePlayer2 == 2:
# #             self.finalSet = True
# #             return True
# #
# #     if self.gamesCastigatePlayer2 == self.targetGames:
# #         if self.gamesCastigatePlayer1 == self.targetGames:
# #             varTiebreakGame = self.playTiebreak()
# #             if self.first_server_to_serve == True:
# #                 if varTiebreakGame == True:
# #                     self.gamesCastigatePlayer1 += 1
# #                     self.finalSet = True
# #                     return True
# #                 else:
# #                     self.gamesCastigatePlayer2 += 1
# #                     self.finalSet = True
# #                     return False
# #             else:
# #                 if varTiebreakGame == True:
# #                     self.gamesCastigatePlayer2 += 1
# #                     self.finalSet = True
# #                     return False
# #                 else:
# #                     self.gamesCastigatePlayer1 += 1
# #                     self.finalSet = True
# #                     return True
# #         if self.gamesCastigatePlayer2 - self.gamesCastigatePlayer1 >= 2:
# #             self.finalSet = True
# #             return False
# #     elif self.gamesCastigatePlayer2 == self.targetGames + 1:
# #         if self.gamesCastigatePlayer2 - self.gamesCastigatePlayer1 == 2:
# #             self.finalSet = True
# #             return False
# #     if self.finalSet == False:
# #         if self.first_server_to_serve == True:
# #             self.first_server_to_serve = False
# #         else:
# #             self.first_server_to_serve = True
# #
# #     # if self.gamesCastigatePlayer2 == self.gamesCastigatePlayer1 and self.gamesCastigatePlayer2 == self.tiebreakGames:
# #     #     variabilaTiebreak = self.playTiebreak()
# #     #     self.finalSet = True
# #     #     if self.first_server_to_serve == True:
# #     #         if variabilaTiebreak == True:
# #     #             self.listaGamesPlayer1.append(1)
# #     #             self.listaGamesPlayer2.append(0)
# #     #             return True
# #     #         else:
# #     #             self.listaGamesPlayer1.append(0)
# #     #             self.listaGamesPlayer2.append(1)
# #     #             return False
# #     #     else:
# #     #         if variabilaTiebreak == True:
# #     #             self.listaGamesPlayer2.append(1)
# #     #             self.listaGamesPlayer1.append(0)
# #     #             return False
# #     #         else:
# #     #             self.listaGamesPlayer2.append(0)
# #     #             self.listaGamesPlayer1.append(1)
# #     #             return True
# #     # elif self.gamesCastigatePlayer2 > self.gamesCastigatePlayer1 and (self.gamesCastigatePlayer2 - self.gamesCastigatePlayer1 >= 2) and self.gamesCastigatePlayer2 >= self.targetGames:
# #     #     self.finalSet = True
# #     #     return False
# #     # elif self.gamesCastigatePlayer2+ self.gamesCastigatePlayer1 < 6 or abs(self.gamesCastigatePlayer1-self.gamesCastigatePlayer2) < 2:
# #     #     if self.first_server_to_serve == True:
# #     #         self.first_server_to_serve = False
# #     #     else:
# #     #         self.first_server_to_serve = True
# #     # elif self.gamesCastigatePlayer1 > self.gamesCastigatePlayer2 and (self.gamesCastigatePlayer1 - self.gamesCastigatePlayer2 >= 2) and self.gamesCastigatePlayer1 >= self.targetGames:
# #     #     self.finalSet = True
# #     #     return True
#
#
# table_data1 = '<div class="column"><table>';
# for (var count = 257; count < 385; count++)
#     {
#         table_data1 += '<tr>';
#     if ((count - 257) === 0)
#     {
#     table_data1 += '<th>Turul 2</th>';
#     }
#     else
#     {
#     table_data1 += '<td>'+employee_data[count]+'</td>';
#     }
#     }
# table_data1 += '</tr>';
# table_data1 += '</table></div>';
# $('#employee_table').html(table_data1);
#
# table_data2 = '<div class="column"><table>';
# for (var count = 385; count < 449; count++)
#     {
#         table_data2 += '<tr>';
#     if ((count - 385) === 0)
#     {
#     table_data2 += '<th>Turul 3</th>';
#     }
#     else
#     {
#     table_data2 += '<td>'+employee_data[count]+'</td>';
#     }
#     }
# table_data2 += '</tr>';
# table_data2 += '</table></div>';
#
# $('#employee_table').html(table_data2);
