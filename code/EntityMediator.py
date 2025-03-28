from code.Const import WIN_WIDTH
from code.Executor import Executor
from code.ExecutorShot import ExecutorShot
from code.Entity import Entity
from code.Falcon import Falcon
from code.FalconShot import FalconShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Executor):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, FalconShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, ExecutorShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Executor) and isinstance(ent2, FalconShot):
            valid_interaction = True
        elif isinstance(ent1, FalconShot) and isinstance(ent2, Executor):
            valid_interaction = True
        elif isinstance(ent1, Falcon) and isinstance(ent2, ExecutorShot):
            valid_interaction = True
        elif isinstance(ent1, ExecutorShot) and isinstance(ent2, Falcon):
            valid_interaction = True

        if valid_interaction:  # if valid_interaction == True:
            if (ent1.rect.right >= ent2.rect.left and ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(executor: Executor, entity_list: list[Entity]):
        if executor.last_dmg == 'FalconShot':
            for ent in entity_list:
                if ent.name == 'Falcon':
                    ent.score += executor.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Executor):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
