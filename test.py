# arr = ['a', 'b']

# obj = dict(enumerate(arr))

# print(obj)
# # for item in obj:
#     # print(item)

# class snake():
#     body = []
#     turns = {}
#
#     def __init__(self, col, pos):
#         self.col = col
#         self.head = cube(pos)
#         self.body.append(self.head)
#         self.dirnx = 0
#         self.dirny = 1
#
#     def move(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#
#             keys = pygame.key.get_pressed()
#             for key in keys:
#                 if keys[pygame.K_LEFT]:
#                     self.dirnx = -1
#                     self.dirny = 0
#                     self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
#                 elif keys[pygame.K_RIGHT]:
#                     self.dirnx = 1
#                     self.dirny = 0
#                     self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
#                 elif keys[pygame.K_UP]:
#                     self.dirnx = 0
#                     self.dirny = -1
#                     self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
#                 elif keys[pygame.K_DOWN]:
#                     self.dirnx = 0
#                     self.dirny = 1
#                     self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
#
#         for i, c in enumerate(self.body):
#             p = c.pos[:]
#             if p is self.turns:
#                 turn = self.turns[p]
#                 c.move(turn[0], turn[1])
#                 if i == len(self.body - 1):
#                     self.turns.pop(p)
#        else:
#            if c.dirnx == -1 and c.pos[0] <= 0:
#                c.pos = (c.rows - 1, c.pos[1])
#            elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
#                c.pos = (0, c.pos[1])
#            elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
#                c.pos = (c.pos[0], 0)
#            elif c.dirny == -1 and c.pos[1] <= 0:
#                c.pos = (c.pos[0]. c.rows - 1)
#            else:
#                c.move(c.dirnx, c.dirny)
#
